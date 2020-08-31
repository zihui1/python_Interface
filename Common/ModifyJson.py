#encoding = utf-8

from Common.HandleJson import *
import json,requests
import time
import traceback
"""
实现：
1.json_txt(dic_json)：json格式，遍历key,value，存储到字典中
2.heck_json_value(dic_json,k,v)json格式，遍历后，替换key的value值
3.data_Json(Sendjson_txt),将json字符串转化为json格式
"""

#json序列化json格式
def data_Json(Sendjson_txt):
    data_json = json.loads(Sendjson_txt)
    # print('data_json: ',data_json)
    return data_json

#遍历json文件所有的key对应的value,存储到一个字典中

dic = {}
def json_txt(dic_json):

    if isinstance(dic_json,dict): #判断是否是字典类型isinstance 返回True,false
        for key in dic_json:
            if isinstance(dic_json[key],dict):#如果dic_json[key]依旧是字典类型
                # print("****key--：%s ,value--: %s"%(key,dic_json[key]))
                #递归调用
                json_txt(dic_json[key])
                dic[key] = dic_json[key]
            else:
                # print("****key1--：%s ,value--: %s"%(key,dic_json[key]))
                dic[key] = dic_json[key]
        return dic


#遍历json字典key值后，查到ke则修改值value
def  check_json_value(dic_json,k,v):
    if isinstance(dic_json,dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
            elif isinstance(dic_json[key],dict):
                check_json_value(dic_json[key],k,v)




if __name__=="__main__":
    data = get_value("login")
    # print(data)
    # json_txt(data)
    time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # check_json_value(data, "transDate", time_stamp)
    # check_json_value(data, "transNonce", str(uuid.uuid1()))
    # json_txt(data)
    # print(type(data))

    headr = get_value("Header", "/Config/header.json")
    url = "http://192.168.31.232/dgjs-api/user/main/login"
    check_json_value(data, "transDate", time_stamp)
    check_json_value(data, "transNonce", str(uuid.uuid1()))
    response = requests.post(url=url, data=json.dumps(data), headers=headr)
    dic = json_txt(response.json())
    print(dic["transNonce"])
    print(response.json())
