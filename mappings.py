"""Doc String."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pickle import load
from mimetypes import guess_type
from json import load


class Config:
    """Doc String."""

    map_filename = 'maps.pk'
    dyn_file = 'test.json'

    def get_fixed_keys(self):
        """Return fixed keys into a dict format."""
        # Processing/filteration of data here and return keys only
        return ['rav', 'nehayadav']

    def get_dynamic_keys(self):
        """Return dynamic keys into a dict format."""
        if guess_type(self.dyn_file)[0].split('/')[1] == 'json':
            # Processing/filteration of data here and return keys only
            return load(open(self.dyn_file)).keys()

        elif guess_type(self.dyn_file)[0].split('/')[1] == 'xml':
            # TODO: implementation of xml to dict
            pass
        elif guess_type(self.dyn_file)[0].split('/')[1] == 'csv':
            # TODO: implementation of xml to dict
            pass
