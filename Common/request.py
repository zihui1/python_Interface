# encoding = utf-8
import requests,json

class request:
    def send_post(self,url,data,header=None):
        response = requests.post(url = url,data = data,headers=header)
        res = response
        return res

    def send_get(self,url,data = None,headers=None):
        response = requests.get(url = url,data = data,headers = headers)
        res = response.text
        return res

    def run_main(self,method,url,data=None,header=None):
        # base_url =
        if 'http' not in url:
            url = 'http://'+url
        if method == "get":
            res = self.send_get(url,data,header)
        else:
            res = self.send_post(url,data,header)
        return res


if __name__ == "__main__":
    url = "http://test.uenpay.com/api/wfb/mobile/chat/doLogin"
    data = {
        "code": "200",
        "password": "qqqq1111",
        "username": "18616726547"
    }
    headrs ={"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8"}
    data1 = json.dumps(data)
    re = request().run_main(method="post", url=url, data=data1, header=headrs)
    print(json.loads(re.text))



