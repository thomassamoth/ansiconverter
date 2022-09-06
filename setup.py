from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ansiconverter",
    version="0.0.2",
    description="Convert any color in RGB or hexadecimal format to ANSI code",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["ansiconverter"],
    author="Thomas Beyet",
    author_email=None,
    url="https://github.com/thomassamoth/ansiconverter",
    package_dir={"": "src"},
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": [
            "pytest>=3.6",
        ],
    },
    project_urls={'source': 'http://github.com/thomassamoth/ansiconverter', }
)
