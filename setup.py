#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup

config = {
        "name": "Prefind",
        "description": (
            "A simple grep-like tool to find files containing given string(s)."),
        "version": "0.2.1",
        "author": "Nikola Pavlović",
        "author_email": "npavlovi@gmail.com",
        "url": "https://github.com/nzp/prefind",
        "packages": ["prefind"],
        "license": "BSD 2-Clause",
        "scripts": ["bin/prefind"],
        "data_files": [
            ("share/doc/prefind", [  # TODO: See what's sensible on Windows.
                "README.rst",
                "LICENSE",
                ])]
        }

setup(**config)
