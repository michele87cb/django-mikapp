# coding=utf-8
# ---------------------------------------------------------------
# Project: mikapp
# Date   : 03/06/2016 09:57
# Author : MikeWil
# Source : _paths.py
# ---------------------------------------------------------------
# MICHELE GUGLIELMI
# ---------------------------------------------------------------
def get_root_dir():
    pathfile = __file__
    pathfile = pathfile.replace('\\', '/')
    pathfile = pathfile.replace('_libs/_paths.py', '')
    return pathfile


def get_cnf_dir():
    return get_root_dir() + '_cnf/'


def get_static_dir():
    return get_root_dir() + 'static/'


_cnfdir = get_cnf_dir()
_rootdir = get_root_dir()
_staticdir = get_root_dir()

