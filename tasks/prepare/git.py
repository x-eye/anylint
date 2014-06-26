#coding=utf-8
import csv
from io import StringIO
import os
from lib.run import run

__author__ = 'x-eye'



def check_directory_empty(path):
    if os.path.exists(path) and os.listdir(path):
        return False
    return True


def clone(repo, path):
    """Clone git repository, checkout it's HEAD"""

    code, out, err = run('git', 'clone', '--quiet',  '--depth', '1', repo, path)

    return code


def checkout(path, revision):
    """"""

    code, out, err = run('git', 'checkout', '--force', '--quiet', revision, cwd=path)

    return code


def parse_branches(data):
    """
    Parse output of git branch -r, eg:
          origin/2.0.X
          origin/HEAD -> origin/master
          origin/develop
          origin/master
          origin/release/2.0.0
          origin/release/2.1.0
    """
    clean_branches = []
    raw_branches = csv.reader(StringIO(data), delimiter=' ')
    for branch in raw_branches:
        branch = list(filter(lambda f: f != '' and f != '*', branch))
        # Handle empty branches
        if len(branch):
            branch = branch[0]
            if branch.startswith('origin/'):
                cut_len = len('origin/')
                slug = branch[cut_len:].replace('/', '-')
                if slug in ['HEAD']:
                    continue
                clean_branches.append((branch, slug))
            else:
                # Believe this is dead code.
                slug = branch.replace('/', '-')
                clean_branches.append((branch, slug))
    return clean_branches


def branches(path):
    code, out, err = run('git', 'branch', '-r', cwd=os.path.abspath(path))
    return parse_branches(out.decode('utf-8'))