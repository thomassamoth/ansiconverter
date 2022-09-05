from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ansiconverter",
    version="0.0.1",
    description="Convert any color in RGB or hexadecimal format to ANSI code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Thomas Beyet",
    author_email="",
    url="https://github.com/thomassamoth/ansiconverter",
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": [
            "pytest>=3.6",
        ],
    },
)
