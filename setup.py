from setuptools import setup, find_packages

setup(
    name="meupacote",
    version="0.1",
    packages=find_packages(),
    author="Seu Nome",
    author_email="seunome@email.com",
    description="Um pacote de saudação",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
