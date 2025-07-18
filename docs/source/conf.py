# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'CEINMS-RT'
copyright = '2023, CEINMS-RT'
author = 'CEINMS-RT'

release = '1.1'
version = '1.1'

# -- General configuration

pygments_style = 'sphinx'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "images/logo-ceinms-rt-white-128.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"
copybutton_here_doc_delimiter = "EOT"
copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

# -- Options for EPUB output
epub_show_urls = 'footnote'
