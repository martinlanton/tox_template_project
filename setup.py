from setuptools import setup, find_packages

name = 'template_project'


setup(name=name,
      version='0.1',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      install_requires=['pytest'])
