from setuptools import setup, find_packages

setup(
    name="analyze-shopify",
    version="0.1.0",
    description="Matatika datasets for tap-shopify",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-shopify/*.yml",
        ]
    },
)
