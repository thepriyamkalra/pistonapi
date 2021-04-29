from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pistonapi",
    version="1.0",
    description="Unofficial Piston API Wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pistonapi"],
    package_dir={
        "pistonapi": "src",
    },
    author="Priyam Kalra",
    author_email="justaprudev@gmail.com",
    url="https://github.com/justaprudev/pistonapi",
    install_requires=[
        "requests",
    ],
)
