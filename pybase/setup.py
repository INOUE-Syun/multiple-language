'配布用パッケージをsetupします'

from setuptools import setup, find_packages

setup(name='pybase',
      varsion='1.0',
      packages=find_packages('src'),
      py_modules=[],
      package_dir={'': 'src'})
