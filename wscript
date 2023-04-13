#! /usr/bin/env python
# encoding: utf-8

APPNAME = "filesystem"
VERSION = "1.5.14"


def build(bld):

    # Path to the source repo
    directory = bld.dependency_node("filesystem-source")

    includes = directory.find_node("include")

    bld(name="filesystem", export_includes=[includes])
