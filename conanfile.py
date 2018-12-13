#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostBimapConan(base.BoostBaseConan):
    name = "boost_bimap"
    url = "https://github.com/bincrafters/conan-bimap"
    lib_short_names = ["bimap"]
    header_only_libs = ["bimap"]
    cycle_group = "boost_cycle_group_d"
    b2_requires = ["boost_cycle_group_d"]
