from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='multi_elo',
    version='1.0.0',
    description='ELO score calculator for more than two players',
    long_description=long_description,
    url='https://github.com/knockoutMice/multi_elo',

    author='Mice Pápai',
    author_email='mice@gorbekor.hu',

    license='Apache-2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Board Games',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='elo elo-score chess ranking multiplayer scoring score rating',

    install_requires=[],
    py_modules=['multi_elo'],
)
