"""Sphinx configuration."""
project = "Tabelir"
author = "Fábio P. Fortkamp"
copyright = "2023, Fábio P. Fortkamp"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
