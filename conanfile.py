#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostBimapConan(base.BoostBaseConan):
    name = "boost_bimap"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-bimap"
    lib_short_names = ["bimap"]
    header_only_libs = ["bimap"]
    b2_requires = [
        "boost_level14group",
    ]
    