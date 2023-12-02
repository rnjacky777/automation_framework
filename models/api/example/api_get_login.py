import requests
from models.api.example.api_get_login_response import ApiGetLoginResponse
#example
class ApiGetLogin():
    url = "http://127.0.0.1:5000/login"

    def get(self, account, password):
        header = None
        payload = {"account": account,
                   "password": self.__hash_password(password)}
        res = requests.get(url=self.url,headers=header,payload=payload)
        return ApiGetLoginResponse(**res)

    def __hash_password(self, password):
        return password+1
