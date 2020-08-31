# encoding = utf-8
from Common.HandleJson import *
from Common.ModifyJson import *
from Common.request import *
def login(name):
    if name =="dgj":
        url = "http://192.168.31.232/dgjs-api/user/main/login"
        headrs = get_value("Header", "/Config/header.json")
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        data = get_value("dgjlogin")
        check_json_value(data, "transDate", time_stamp)
        check_json_value(data, "transNonce", str(uuid.uuid1()))
        respone = request().run_main("post", url, json.dumps(data), header=headrs)
        dic = json_txt(respone.json())
        return dic
if __name__ == "__main__":
    print(login("dgj"))
