from setuptools import setup, find_packages

install_requires = [
    "snowflake-connector-python",
    "pyspark"
]

test_requires = ["pytest", "pytest-mock"]

setup(
    name="default_package",
    version="0.0.0",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={ "tests": test_requires},
)
