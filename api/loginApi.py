import requests

import data
from config import IP, HEADERS


class MtxLogin(object):
    def __init__(self):
        self.url = IP +"/mtx/index.php?s=/index/user/login.html"

    def login(self,session,data):
        resp_login = requests.post(self.url,data=data,headers = HEADERS)
        return resp_login
    def login_success(self,session):
        '''
        登录成功的请求
        :param session:
        :return:
        '''
        data = {"accounts": "yaoyao", "pwd": "yaoyao"}
        resp_login = requests.post(self.url,data=data,headers = HEADERS)

        return resp_login