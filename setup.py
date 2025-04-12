from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()


setup(
    name="contasRenato",
    version="0.0.1",
    author="Renato Freitas da Silveira",
    description="pacote para calcular fatorial e combinação simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenatoFreitas1991/pacoteImagemRenato.git",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.12",
)
