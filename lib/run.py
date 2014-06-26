#coding=utf-8
import os
import subprocess

__author__ = 'x-eye'


def run(*args, **kwargs):
    """
    :param args: list of command and args. See `subprocess` docs
    """
    params = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd='.', shell=False, env=os.environ.copy())
    params.update(kwargs)
    process = subprocess.Popen(args, **params)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr