import unittest
from Common.HTMLTestRunner import HTMLTestRunner
from Common.request import *
from Common.HandleJson import *
from Common.ModifyJson import *
from Common.Oracle import *
import os,json

class Test1(unittest.TestCase):
    headr = {}

    def test_doLogin(self):
        # 登录
        self.url = "http://test.uenpay.com/api/wfb/mobile/chat/doLogin"
        self.data = {
            "code": "200",
            "username": "13761917640"
        }
        globals()['headr'] = get_value("Header", "/Config/header.json")
        self.data1 = json.dumps(self.data)
        re = request().run_main(method="post", url=self.url, data=self.data1, header=globals()['headr'] )
        Authorization = json_txt(re.json())["token_type"] + json_txt(re.json())["access_token"]
        check_json_value(globals()['headr'] , "Authorization", Authorization)
        # print(globals()['headr'] )
        print(json.dumps(re.json(), ensure_ascii=False, indent=2, separators=(',', ':')))

    def test_queryBill(self):
        # 获取账单列表
        self.url = "http://test.uenpay.com/api/wfb/wfbuserbill/queryBill"
        self.data = {
            "page": 1,
            "rows": 10
        }
        self.data1 = json.dumps(self.data)
        re = request().run_main(method="post", url=self.url, data=self.data1, header=globals()['headr'] )
        print(json.dumps(re.json(), ensure_ascii=False, indent=2, separators=(',', ':')))


    def test_queryBillDetail(self):
        # 获取账单详细
        self.url = "http://test.uenpay.com/api/wfb/wfbuserbill/queryBillDetail"
        self.data = {
                    "page": 1,
                    "rows": 10,
                    "tradeNo" :"201130000000001043",
                    "type" : 1
                    }
        self.data1 = json.dumps(self.data)
        re = request().run_main(method="post", url=self.url, data=self.data1, header=globals()['headr'] )
        print(json.dumps(re.json(), ensure_ascii=False, indent=2, separators=(',', ':')))

    def test_queryBalanceDetail(self):
        # 获取余额明细
        self.url = "http://test.uenpay.com/api/wfb/wfbuserbill/queryBalanceDetail"
        self.data = {
                      "page": 1,
                      "rows": 10,
                      "type": "100"
                    }
        self.data1 = json.dumps(self.data)
        re = request().run_main(method="post", url=self.url, data=self.data1, header=globals()['headr'])
        print(json.dumps(re.json(), ensure_ascii=False, indent=2, separators=(',', ':')))

    def test_queryPayeeBill(self):
        # 获取收款列表
        self.url = "http://test.uenpay.com/api/wfb/wfbuserbill/queryPayeeBill"
        self.data = {
            "page": 1,
            "rows": 10
        }
        self.data1 = json.dumps(self.data)
        re = request().run_main(method="post", url=self.url, data=self.data1, header=globals()['headr'])
        print(json.dumps(re.json(), ensure_ascii=False, indent=2, separators=(',', ':')))

if __name__ == '__main__':
    unittest.main()