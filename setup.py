"""
newscomb
~~~~~~~~
Topic modeling for Hacker News articles
"""

from setuptools import setup, find_packages


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        result = f.read().splitlines()
    return result

setup(
    name='newscomb',
    version='0.0.1',
    url='https://github.com/reeddunkle/Hacker_News_Topic_Model',
    author='Reed Dunkle',
    author_email='reeddunkle@gmail.com',
    description='Hacker News Topic Modeling',
    long_description='',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any')