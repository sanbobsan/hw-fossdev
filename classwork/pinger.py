from datetime import datetime, timedelta

from niquests import Response, Session


class Pinger:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._session = self._create_session()

    def _create_session(self) -> Session:
        session = Session()
        session.headers = {
            "User-Agent": "pinger/0.1.0",
            "Connection": "keep-alive",
        }
        return session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self._session.close()

    def ping(self, params: dict) -> Response:
        r: Response = self._session.get(url=self.base_url, params=params, stream=True)
        return r


def main() -> None:
    current_date: datetime = datetime.now()

    with Pinger("https://simurg.space/gen_file") as pinger:
        while True:
            date_str: str = current_date.strftime("%Y-%m-%d")
            params: dict = {
                "data": "obs",
                "date": date_str,
            }

            response: Response = pinger.ping(params)

            if response.ok:
                print(response)
                break

            print(f"{date_str}: <{response.status_code}>")
            current_date -= timedelta(1)


if __name__ == "__main__":
    pass
