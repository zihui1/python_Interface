# encoding = utf-8
import json
from Common.HandleJson import get_value
from deepdiff import DeepDiff

def handle_result(url,code):
    data = get_value(url)
    if data !=None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def get_result_json(url,status):
    data= get_value(url)
    if data!=None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

def handle_result_json(dict1,dict2):
    # json格式校验
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict=DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        # print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False

if __name__ == "__main__":
    dict1 = {"aaa": "bbb1", "ccc": "ddd"}
    dict2 = {"aaa": "bbb", "ccc1": "ddd"}
    # print(handle_result("data",3))
    print(type(dict1))
    print(handle_result_json(dict1,dict2))