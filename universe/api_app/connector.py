import requests
import json

def beauty_console_view(data):
    return "\n".join([f"{i}:{data[i]['name']}" for i in range(len(data))])

def get_item_id(data, name_data):
    data_str = beauty_console_view(data)
    print(data_str)
    return data[int(input(f"Choose {name_data}:"))]["id"]

class Connector:

    server = "http://127.0.0.1:8000"
    api = "api"
    auth = "rest-auth/login"
    path_to_cred = r"E:\PITON_SHHHH\DJANGGGGGGGGO\TO_INFINITY_UNIVERSE\Myproject_main\universe\api_app\auth.json"

    def __init__(self):
        self.session = requests.session()
        cred = json.load(open(self.path_to_cred, 'r'))
        res = self.session.post(self.auth_url, json=cred)
        self.session.headers.update({
            "Authorization": "Token " + res.json()["key"],
        })

    def url_maker(self,*items):
        return "/".join([self.server, *items])+"/"

    @property
    def api_url(self):
        return self.url_maker(self.api)

    @property
    def auth_url(self):
        return self.url_maker(self.auth)
    
    def get_list(self, lc_model:str):
        res = self.session.get(self.url_maker(self.api, lc_model))
        return res.json()

    def create(self, lc_model:str, data):
        res = self.session.post(self.url_maker(self.api, lc_model), json=data)
        print(self.server)
        print(self.api)
        print(self.auth)
        print(self.auth_url)
        print(self.api_url)
        print(res.status_code)
        print(lc_model)
        print(self.url_maker(self.api, lc_model))
        return res.json()
