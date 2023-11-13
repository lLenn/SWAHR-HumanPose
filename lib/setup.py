from setuptools import setup, find_packages

packages = find_packages(where="SWAHR")
setup(
    name="SWAHR",
    packages=["SWAHR"] + [f"SWAHR.{package}" for package in packages],
)