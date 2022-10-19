import pytest
import json
import yaml


users_json = 'admin_users.json'
users_yaml = 'admin_users.yaml'

# regular_users_json = 'regular_users.json'
# regular_users_yaml = 'regular_users.yaml'




# users_json = regular_users_json
# users_yaml = regular_users_yaml



class Test:

    def ffile(users_json):
        return open(users_json)

    def load_data_json(fname):
        # Load data
        return json.load(fname)

    def load_data_yaml(fname):
        with open(fname) as f:
            my_dict = yaml.safe_load(f)
            return my_dict

        return None

    def close_file(fname):

        # Closing file
        fname.close()

    def check_data(data):

        for i in data:
            if i['id'] is not None and i['name'] is not None:
                pass
            else:
                return False

        return True


    def validation_one(users_json):

        name = Test.ffile(users_json)
        data = Test.load_data_json(name)

        assert Test.check_data(data)== True

        Test.close_file(name)

    def validation_two(user_yaml):
        data = Test.load_data_yaml(user_yaml)

        assert Test.check_data(data) == True


    def validation_three(data1,data2):

        for e in data1:
            if e in data2:
                pass
            else:
               return False

        return True




Test.validation_one(users_json)

Test.validation_two(users_yaml)

name = Test.ffile(users_json)

data1 = Test.load_data_json(name)
data2 = Test.load_data_yaml(users_yaml)

assert Test.validation_three(data1,data2)
