# encoding = utf-8
import json
from Config.VarConfig import *
import requests,uuid,time

def read_json(file_name=None):
    if file_name == None:
        file_path = parentDirPath+"/Config/user_data.json"
    else:
        file_path = parentDirPath+file_name
    with open(file_path,encoding='UTF-8') as f:
        data = json.load(f)
    return data

def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)


if __name__ == "__main__":
    print(get_value("transNonce"))
