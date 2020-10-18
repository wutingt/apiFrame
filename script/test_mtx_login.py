import allure
import pytest
import requests

from api.loginApi import MtxLogin
from tools import anlyze_data

class TestLogin:
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口对象

        self.login_obj = MtxLogin()

    # 测试登录成功的测试用例
    def test_login_success(self):
        resp_login = self.login_obj.login_success(self.session)
        assert resp_login.josn().get("msg") == "登录成功"

    # 参数化 用yml文件去保存我们的测试数据
    # data_list =[{},{}<{}]
    @pytest.mark.parametrize("args",anlyze_data('login_data','test_login'))
    @allure.title('登录异常，测试数据是：{args}')
    def test_login_error(self,args):
        data ={'accounts':args['accounts'],'pwd':args['pwd']}
        resp_login = self.login_obj.login(self.session,data)
        assert resp_login.json().get("msg")==args['exp']

