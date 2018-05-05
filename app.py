"""Doc string."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, render_template_string
from flask_restful import Api, Resource
from os.path import abspath
from pickle import dump
from json import loads
from operator import itemgetter
from fuzzywuzzy import process
from mappings import Config, RED


app = Flask(__name__)
api = Api(app)

fixed_keys = None
dynamic_keys = dict()


@app.route('/')
def index():
    """Doc string."""
    data = GenerateKeys().generate()
    return render_template('index.html', data=data)


class HandleInput(Resource):
    """Doc string."""

    @staticmethod
    def post():
        """Doc string."""
        mapping_filepath = '/'.join(abspath(__file__).split('/')
                                    [:-1] + ['maps.pk'])
        try:
            dump({item: request.form.get(item)
                for item in fixed_keys}, open(mapping_filepath, 'wb'))
        except TypeError:
            # TODO: known issuee to be fixed soon.
            print(RED.format("Clear Everything and reload page agian."))
        return {
            "status": "success",
            "filePath": mapping_filepath
        }


class GenerateKeys(Config):
    """Doc String."""

    def generate(self):
        """Doc String."""
        global fixed_keys, dynamic_keys
        fixed_keys = self.get_fixed_keys()
        _dynamic_keys = self.get_dynamic_keys()
        for item in fixed_keys:
            dynamic_keys[item] = (i[0]
                                  for i in process.extract(item, _dynamic_keys))
        return {'fixed_keys': fixed_keys, 'dynamic_keys': dynamic_keys}


if __name__ == '__main__':
    api.add_resource(HandleInput, '/process', endpoint='process')
    app.run()
