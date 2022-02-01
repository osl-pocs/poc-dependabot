"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Ivan Ogasawara",
    author_email='ivan.ogasawara@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="PoC Dependabot",
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='poc_dependabot',
    name='poc_dependabot',
    packages=find_packages(include=['poc_dependabot']),
    test_suite='tests',
    url='https://github.com/xmnlab/poc_dependabot',
    version='1.0.0',
    zip_safe=False,
)
