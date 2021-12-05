from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tcm_stunner/__init__.py
from tcm_stunner import __version__ as version

setup(
	name="tcm_stunner",
	version=version,
	description="For Testing",
	author="Soumen Biswas",
	author_email="soumen@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
