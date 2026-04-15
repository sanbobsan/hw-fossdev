import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

project = "sales"
copyright = "2026, sanbob"
author = "sanbob"
release = "0.0.1"


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",  # атоматический сбор docstring'ов из кода
    "sphinx.ext.napoleon",  # поддержка стиля docstring'ов Google и NumPy
    "sphinx.ext.autosummary",  # автоматическое создание оглавления для модулей
    "sphinx.ext.viewcode",  # добавление ссылок на исходный код в документацию
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns: list[str] = []

language = "ru"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
