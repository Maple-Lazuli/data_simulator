import yaml
import os


class Specification:
    def __init__(self, yaml_path):
        if not os.path.exists(yaml_path):
            raise Exception(f"{yaml_path} not found.")

        with open(yaml_path) as file_in:
            self.spec = yaml.safe_load(yaml_path)

        self.components = []

    def get_spec(self):
        return self.spec

    def get_repr(self):
        # return the repr of the individual components
        pass

    def get_spec_components(self):
        pass