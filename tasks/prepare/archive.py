#coding=utf-8
import subprocess

__author__ = 'x-eye'


class ArchiveFormatError(Exception):
    pass


ext_map = (
    ('.tar.bz2', 'tar jxf %(src)s'),
    ('.tar.gz', 'tar zxf %(src)s'),
    ('.tgz', 'tar zxf %(src)s'),
    ('.gz', 'gzip -d %(src)s'),
    ('.zip', 'gzip -d %(src)s'),
)


def get_unpacker(src):
    for ext, unpacker in ext_map:
        if src.endswith(ext):
            return unpacker
    raise ArchiveFormatError('"%s" extension does not match any known unpacker' % ext)


def unpack(src, path):
    unpacker = get_unpacker(src)
    command = unpacker % {'src': src}
    subprocess.Popen(command, cwd=path)
