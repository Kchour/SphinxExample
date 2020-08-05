.. example_sphinx_project documentation master file, created by
   sphinx-quickstart on Wed Aug  5 13:45:09 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to example_sphinx_project's documentation!
==================================================

.. toctree::
   
   readme_link
   todo_link

.. autosummary::
   :toctree: _autosummary
   :caption: API Reference
   :template: custom-module-template.rst
   :recursive:

   example_package
