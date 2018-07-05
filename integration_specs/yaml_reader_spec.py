# -*- coding: utf-8 -*-

import os
import yaml
import tempfile

from mamba import description, context, it, before, after
from expects import expect, equal, be, be_an, raise_error

from infcommon.yaml_reader.yaml_reader import YamlReader
from infcommon.info_container.info_container import InfoContainer


KEY = 'key'
VALUE = 'value'
NON_EXISTING_KEY = 'non_existing_key'


with description('YamlReader') as self:
    def _generate_file_and_return_name(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as keyvalue_file:
            keyvalue_file.write(yaml.dump({KEY: VALUE}))

            return keyvalue_file.name

    with before.all:
        self.yaml_file = self._generate_file_and_return_name()
        self.yaml_reader = YamlReader(self.yaml_file)

    with after.all:
        os.unlink(self.yaml_file)

    with context('given a yaml file'):
        with context('when obtaining an info container'):
            with it('returns an info container'):
                result = self.yaml_reader.get_info_container()

                expect(result).to(be_an(InfoContainer))

            with it('contains keyvalues from yaml file'):
                result = self.yaml_reader.get_info_container()

                expect(result).to(equal(InfoContainer({KEY:VALUE}, return_none=True)))


    with context('given a yaml_reader object with properties loaded in it'):
        with context('when accesing an attribute'):
            with context('that exists'):
                with it('returns its value'):
                    expect(self.yaml_reader[KEY]).to(equal(VALUE))

            with context('that does NOT exist'):
                with it('raises a KeyError exception'):
                    def accesing_a_non_existing_attribute():
                        self.yaml_reader[NON_EXISTING_KEY]

                    expect(accesing_a_non_existing_attribute).to(raise_error(KeyError))

        with context('when getting a value from a key'):
            with context('that exists'):
                with it('returns its value'):
                    expect(self.yaml_reader.get(KEY)).to(equal(VALUE))

            with context('that does NOT exist'):
                with it('returns None'):
                    expect(self.yaml_reader.get(NON_EXISTING_KEY)).to(be(None))
