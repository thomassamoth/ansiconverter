from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ansiconverter",
    version="2.0.0",
    description="Convert any colour, from RGB or hexadecimal format, to ANSI code.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # py_packages=["ansiconverter","converter"],
    packages=find_packages() + ["test"],
    author="Thomas Beyet",
    author_email=None,
    url="https://github.com/thomassamoth/ansiconverter",
    # package_dir={"": "ansiconverter"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": [
            "pytest>=3.6",
        ],
    },
    project_urls={
        "source": "http://github.com/thomassamoth/ansiconverter",
    },
    python_requires=">=3.6",
)
