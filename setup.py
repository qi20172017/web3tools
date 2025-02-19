"""Web3tools package setup configuration."""

from setuptools import find_packages, setup

setup(
    name="web3tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "web3>=6.15.1",
        "eth-account>=0.11.0",
        "eth-utils>=2.3.1",
        "python-dotenv>=1.0.1",
    ],
    author="Minner",
    author_email="xiaoqideguge@gmail.com",
    description="A collection of Web3 tools",
    keywords="web3, ethereum, blockchain",
    python_requires=">=3.9",
)
