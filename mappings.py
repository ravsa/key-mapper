"""Doc String."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pickle import load as pload
from mimetypes import guess_type
from json import load

MAPPED_KEYS = None
map_filename = 'maps.pk'

RED = "\033[31m{}\033[39m"


class Config:
    """Doc String."""

    dyn_file = 'test.json'

    def get_fixed_keys(self):
        """Return fixed keys into a dict format."""
        # TODO: Processing/filteration of data here and return keys only
        return ['rav', 'nehayadav']

    def get_dynamic_keys(self):
        """Return dynamic keys into a dict format."""
        if guess_type(self.dyn_file)[0].split('/')[1] == 'json':
            # TODO: Processing/filteration of data here and return keys only
            return load(open(self.dyn_file)).keys()

        elif guess_type(self.dyn_file)[0].split('/')[1] == 'xml':
            # TODO: Processing/filteration of data here and return keys only
            pass

        elif guess_type(self.dyn_file)[0].split('/')[1] == 'csv':
            # TODO: Processing/filteration of data here and return keys only
            pass


def init():
    """Doc String."""
    global MAPPED_KEYS
    try:
        with open(map_filename, 'rb') as file:
            MAPPED_KEYS = pload(file)
    except FileNotFoundError:
        pass


def get_key(key):
    if MAPPED_KEYS:
        _resp = MAPPED_KEYS.get(key)
        if not _resp:
            raise ValueError(RED.format(
                "No Dynamic key is mapped for the key `{}`".format(key)))
        return _resp
    else:
        print(RED.format("key is not mapped yet please log into http://0.0.0.0:5000"))


init()
