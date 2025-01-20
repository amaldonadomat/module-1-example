from setuptools import setup, find_packages

setup(
    name="python-package",
    version="0.1.0",
    author="Alvaro Maldonado",
    description="An example Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amaldomat/module-1-example",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # List your dependencies here, e.g.:
        # "numpy>=1.19.0",
    ],
)