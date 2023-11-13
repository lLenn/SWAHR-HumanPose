from setuptools import setup, find_packages

packages = find_packages(where="lib")
print(packages)
setup(
    name="SWAHR",
    packages=["SWAHR"] + [f"SWAHR.{package}" for package in packages],
    package_dir={
        "": "lib"
    }
)