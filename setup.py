from setuptools import setup, find_packages

name = 'template_project'
author = "Martin L'Anton"
author_email = "lantonmartin@gmail.com"
url = "https://github.com/martinlanton/ComponentAssembler"

setup(
    name=name,
    version='0.1.0',
    author=author,
    author_email=author_email,
    url=url,
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'pytest<=4.6;python_version<"3"',
        'pytest;python_version>"3"',
    ]
)
