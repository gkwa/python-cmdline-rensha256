# -*- coding: utf-8 -*-

__version__ = "0.1.1"

from hashlib import sha256
import sys
import os
import logging
import pathlib


def main():
    logger = logging.getLogger('rensha256')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('rensha256.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    filesList = [i.strip() for i in sys.stdin.readlines()]

    for path in filesList:
        if not os.path.exists(path):
            logger.debug("file %s not found" % path)
        else:
            logger.debug("original file %s exists" % path)
            original = pathlib.Path(path)
            original.resolve()
            parentdir = original.parent.absolute()
            ext = original.suffix
            f = open(path, 'rb')
            with f:
                sha = sha256(f.read()).hexdigest()
            newfile = '%s%s' % (sha, ext)
            newpath = os.path.join(parentdir, newfile)
            logger.debug('sha256: %s' % sha)
            logger.debug('dir: %s' % parentdir)
            logger.debug('ext: %s' % ext)
            if os.path.exists(newpath):
                logger.warn(
                    'skipping file %s because target destination already exists %s' %
                    (original.absolute(), newpath))
            else:
                logger.debug('mv "%s" "%s"' % (original.absolute(), newpath))
                os.rename(path, newpath)
