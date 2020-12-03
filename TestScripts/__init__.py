#encoding = utf-8
from Common.ParseExcel import ParseExcel
from Config.VarConfig import *
from Common.Log import Log
from Common.request import *
from Common.HandleJson import *
from Common.HandleResult import *
from Common.ModifyJson import *
from Common.login import *
import time
import traceback
import unittest

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)
log = Log()
