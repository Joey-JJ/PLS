import json


class JSON_handler:
    def save_file(json_dict: dict, filename: str):
        """
        Saves a dictionary to a json file, 
        takes in the dict and the name of the file (with or without the .json extension). 
        Returns an error if filename already exists.
        """
        if filename[-5:] != '.json':
            filename += '.json'
        with open(filename, 'x') as file:
            json.dump(json_dict, file, indent=4)

    def load_file(filename: str) -> dict:
        """
        Loads a json file and returns it as a dictionary.
        Only takes filename as argument (with or without .json extension)
        Throws error if file does not exist.
        """
        if filename[-5:] != '.json':
            filename += '.json'
        with open(filename, 'r') as file:
            json_dict = json.load(file)
        return json_dict
