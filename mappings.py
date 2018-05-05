"""Doc String."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pickle import load as pload
from mimetypes import guess_type
from json import load
from xmltodict import parse
from csv import DictReader

MAPPED_KEYS = None
map_filename = 'maps.pk'

RED = "\033[31m{}\033[39m"


class Config:
    """Doc String."""

    dyn_file = 'test.json'

    def get_fixed_keys(self):
        """Return fixed keys into a dict format."""
        # TODO: Processing/filteration of data here and return keys only
        # TODO define your fixed keys here in list/tuple
        return ('someKey1', 'someKey2', 'someKey3')

    def get_dynamic_keys(self):
        """Return dynamic keys into a dict format."""
        if guess_type(self.dyn_file)[0].split('/')[1] == 'json':
            # TODO: Processing/filteration of data here and return keys only
            with open(self.dyn_file) as file:
                return load(file).keys()

        elif guess_type(self.dyn_file)[0].split('/')[1] == 'xml':
            # TODO: Processing/filteration of data here and return keys only
            with open(self.dyn_file) as file:
                xml_data = parse(file.read().strip(), dict_constructor=dict)
                return xml_data.get('doc').keys()

        elif guess_type(self.dyn_file)[0].split('/')[1] == 'csv':
            # TODO: Processing/filteration of data here and return keys only
            with open(self.dyn_file) as file:
                reader = DictReader(file)
                # returns column names in csv
                return reader.fieldnames


def init():
    """Doc String."""
    global MAPPED_KEYS
    try:
        with open(map_filename, 'rb') as file:
            MAPPED_KEYS = pload(file)
    except FileNotFoundError:
        pass


def get_key(key):
    """Doc String."""
    if MAPPED_KEYS:
        _resp = MAPPED_KEYS.get(key)
        if not _resp:
            raise ValueError(RED.format(
                "No Dynamic key is mapped for the key `{}`".format(key)))
        return _resp
    else:
        print(RED.format("key is not mapped yet please log into http://0.0.0.0:5000"))


init()
