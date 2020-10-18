import config
# 提交订单的接口

class Order:
    def __init__(self):
        self.url =config.IP + ''

    def order(self,session,headers):
        data= {}

        resp_order = session.post(self.url, data=data, headers=headers)
       jump_url = resp_order.json().get('data').get('jump_url')

