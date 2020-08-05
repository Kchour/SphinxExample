# ExampleSphinx

Sphinx is an open source document generation tool for python projects. You can create really elegant html or even pdf documents for your code. Though Sphinx is a great tool, it can be overwhelming to set up. 

This repo will help you setup Sphinx

# Requirements
- Python 3. However, it is still possible to document python2 code with sphinx-python3 
- Sphinx
- m2r2
- sphinx-rtd-theme

Install requirements by using 
```
python3 -m pip install -r requirements.txt
```
Note: Code must be documented using `docstrings`. I have opted for Googlestyle docstrings

# Instructions
- Clone this repo to your computer
- Create an empty `doc` folder (delete the one already present here)
- Cd to `doc` and run sphinx's quickstart command `$ sphinx-quickstart`
- Say yes to `Separate source and build directories (y/n) [n]: `
- Name your project, I'll call mine "example_sphinx_project"
- Give your name
- Give a version number (I try to follow semantic versioning X.Y.Z)
- Hit enter on language (if using english)

Your terminal will look something like the following:


## Edit `conf.py`
Remember that Sphinx is not totally automatic, so we need to tune a few settings for it to work. Using your favorite editor, open `doc/source/conf.py`
- Uncomment lines 13-15, so sphinx can actually find your module. Now change to the following
```
import os
import sys
sys.path.insert(0, os.path.abspath('../..')) # Where-ever your module is located
``` 
- Find the `extensions` and change to the following
```
extensions = [
        'm2r2',
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx.ext.viewcode',
        'sphinx.ext.todo',
        'sphinx.ext.autosummary',
]
autosummary_generate = True			#Added this too
source_suffix = ['.rst', '.md']		#Added this too
```

- Finally, let's change the `html_theme`
```
html_theme = 'sphinx_rtd_theme'
```

- Save and close!


Next we want 

## Edit `index.rst`

We will also need to edit `index.rst`. Do recall that .rst extension refers to "restructuredtext", which is an alternative to markdown style readme's you may be used to. 

- Change it so that 'index.rst' looks like the following:

```

.. toctree::

	readme_link
	todo_link

.. autosummary::
	:toctree: _autosummary
	:caption: API Reference
	:template: custom-module-template.rst
	:recursive:

	example_package

```

Note that 'example_module' is the name of our module! (Please delete the extra space in front of each line)

## Copy *_link.rst files

You'll notice that we have 'README.md' and 'TODO.md' files. Can sphinx use them? The answer is yes, but you have to add a few files

- Copy the `*_link.rst` files from `misc/source` to `doc/source`. This helps sphinx locate the `.md` files and convert them to `.rst` format

## Copy template files

The latest version of sphinx (at the time of this writing) has the abiility to recursively scan your module files and generate nice html summaries, a feature called "autosummary". To use the autosummary recursive option, we need to provide a format for sphinx (courtesy of (link)[https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion]). 

- Copy the contents from `misc/_template` to `doc/source/_template`. You may have to create a new folder if `_template` doesn't already exist

## Make

Now all that is needed is to tell sphinx to build the documentation
- `$ cd doc`
- `$ make html`


## View html

Go to `doc/build/html` and open `index.html` with your browser. DONE!

