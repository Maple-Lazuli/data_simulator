from data_simulator.integer import U, S
from data_simulator.string import Unicode

import yaml
import os
import re


def get_component_from_spec(default_endian, spec):
    comment = spec['id'] if 'id' in spec.keys() else ""
    if "type" in spec.keys():
        t = spec['type']
        if t[0] == 'u':
            size = get_size(t)
            endian = get_endian(t) if get_endian(t) is not None else default_endian
            return U(1, size, endian, comment)
        if t[0] == 's':
            size = get_size(t)
            endian = get_endian(t) if get_endian(t) is not None else default_endian
            return U(1, size, endian, comment)
    else:
        # handle case when spec is not provided.
        pass


def process_spec(spec):
    default_endian = spec['meta']['endian']
    components = []
    for comp in spec['seq']:
        comp_t = comp['type']
        if comp_t in spec['types']:
            for sub_comp in spec['types'][comp_t]['seq']:
                processed_field = get_component_from_spec(default_endian, sub_comp)
                components.append(processed_field)
        else:
            processed_field = get_component_from_spec(default_endian, comp)
            components.append(processed_field)
    return components


def get_size(t):
    i = re.search(r"\d+", t)
    if i is not None:
        return i.group(0)
    else:
        # TODO: find the default
        return 1


def get_endian(t):
    i = re.search(r"le", t)
    if i is not None:
        return "le"
    i = re.search(r"be", t)
    if i is not None:
        return "be"
    return None


class Specification:
    def __init__(self, yaml_path):
        if not os.path.exists(yaml_path):
            raise Exception(f"{yaml_path} not found.")

        with open(yaml_path) as file_in:
            self.spec = yaml.safe_load(file_in)

        self.components = process_spec(self.spec)

    def get_spec(self):
        return self.spec

    def get_repr(self):
        # return the repr of the individual components
        pass

    def get_spec_components(self):
        return self.components
