from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.simkintr',
      version=version,
      description="A theme for Tim Simkins' Website",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("HISTORY.md")).read(),
      classifiers=[],
      keywords='',
      author='Tim Simkins',
      author_email='tim.simkins@tandj.net',
      url='https://github.com/tsimkins/plonetheme.simkintr',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="",
      )
