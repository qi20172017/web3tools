from setuptools import setup, find_packages

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
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of Web3 tools",
    keywords="web3, ethereum, blockchain",
    python_requires=">=3.9",
) 