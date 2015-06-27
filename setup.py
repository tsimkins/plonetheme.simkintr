from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.simkintr',
      version=version,
      description="A theme for Tim Simkins' Website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
