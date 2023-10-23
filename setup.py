from setuptools import setup, find_packages

setup(
    name="iconize",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "iconize = Iconize:main",
        ],
    },
)
