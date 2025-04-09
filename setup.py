from setuptools import setup, find_packages

setup(
    name="pacote_imagem",
    version="0.1",
    packages=find_packages(),
    author="Diego Venâncio",
    author_email="diegodevenancio@gmail.com",
    description="Um pacote de imagens",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
