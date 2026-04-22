.PHONY: create-structure create-venv test-pytest check-requirements

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md docs/README.md 
	touch setup.py requirements.txt
	echo "pipreqs" > requirements.txt

create-venv:
	python3 -m venv .venv

test-pytest:
	python3 -m pytest

check-requirements:
	pip install pipreqs
	pipreqs --force .
