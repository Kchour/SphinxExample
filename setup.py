import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_package",
    version="0.0.1",
    author="Kenny Chour",
    author_email="ckennyc@tamu.edu",
    description="Example for setting up sphinx",
    long_description="Example contains a single module with two submodules",
    long_description_content_type="text/markdown",
    url="https://github.com/Kchour/SphinxExample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
