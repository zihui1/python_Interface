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

    def run_main(self,method,url,data,header=None):
        # base_url =
        if 'http' not in url:
            url = 'http://'+url
        if method == "get":
            res = self.send_get(url,data,header)
        else:
            res = self.send_post(url,data,header)
        return res


if __name__ == "__main__":
    url = 'www.baidu.com'

    request().run_main('get',url)




