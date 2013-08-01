import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='camlipy',
    version='0.0.0',
    author='Thomas Sileo',
    author_email='thomas.sileo@gmail.com',
    description='',
    license='MIT',
    keywords='camlistore storage backups blob',
    url='https://github.com/tsileo/camlipy',
    packages=find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    long_description=read('README.rst'),
    install_requires=['requests'],
    test_suite="camlipy.tests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Archiving :: Backup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)