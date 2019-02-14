"""Python Package Definition."""

import os
from setuptools import find_packages, setup


root = os.path.dirname(__file__)
src = os.path.relpath(os.path.join(root, 'python'))

readme = os.path.join(root, 'README.md')
with open(readme) as readme_file:
    pypi_description = readme_file.read()

setup(
    name='bio',
    version='0.1.0',
    description='Python Profiler',
    long_description=pypi_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ylathouris/bio',
    author='Yani Lathouris',
    author_email='ylathouris@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    keywords='io, load, dump, read, write, parse, format, utils',
    project_urls={
        #'Documentation': '',
        'Say Thanks!': 'http://saythanks.io/to/ylathouris',
        'Source': 'https://github.com/ylathouris/bio',
        'Tracker': 'https://github.com/ylathouris/bio/issues',
    },
    package_dir={'': src},
    packages=find_packages(src),
    install_requires=[],
)
