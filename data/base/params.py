import yaml, os
from ruamel.yaml import YAML


class ConfigurationYaml:
    def __init__(
        self,
        mapping: int = 2,
        sequence: int = 4,
        offset: int = 2,
        default_fs: bool = False,
        enc: str = "utf-8",
    ) -> None:
        yaml2 = YAML()
        yaml2.indent(mapping=mapping, sequence=sequence, offset=offset)
        yaml2.default_flow_style = default_fs
        yaml2.encoding = enc
        self.yaml_conf = yaml2


class UGUtils:
    def __init__(self, yaml_file: str) -> None:
        self.path = yaml_file
        self.data = self.get_yaml()
    def get_yaml(self) -> dict:
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as file:
                file.write("")

        with open(self.path, encoding="utf-8") as file:
            data = yaml.safe_load(file)

            if not data:
                return {}
            return data


    def update_yaml(self, data: dict):
        yaml_config = ConfigurationYaml().yaml_conf
        with open(self.path, "w", encoding="utf-8") as file:
            data = yaml_config.dump(data, file)

        if data:
            return data
        return {}
    
    
class Params:
    def __init__(self, yaml_path : str) -> None:
        self.yaml = UGUtils(yaml_path)
        self.data = self.yaml.get_yaml()
        
        self.MY_INSTAGRAM_ID : str = self.data.get('MY_INSTAGRAM_ID')
        self.PUBLIC_REPLAY_ALLOW : bool = self.data.get('PUBLIC_REPLAY_ALLOW', True)
    
    def update(self, data : dict = None, **args) -> bool:
        if data:
            self.yaml.update_yaml(data)

            self.data = data
            return True

        if args:
            yaml_data = self.yaml.get_yaml()
            yaml_data.update(args)
            self.yaml.update_yaml(yaml_data)

            self.data = yaml_data
            return True
        
        return False


if __name__ == '__main__':
    db = Params('test.yaml')

    db.update(blah = 'salom')
    print(db.data)
    