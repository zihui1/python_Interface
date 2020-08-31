# encoding = utf-8
import os
# 获取当前父级绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LogPath = parentDirPath+u"\\Log\\"
# 存放数据文件存放绝对路径
dataFilePath = parentDirPath+u"\\Data\\cas.xlsx"



# 数据源表中，是否执行列对应的数字编号
testStep_testCaseName =2
testStep_testStepSheetName =3
testStep_isExecute =4
testStep_runTime =5
testStep_testResult = 6


#用例步骤是否执行列对应的数字编号
testCase_id = 1
testCase_description = 2
testCase_isExecute = 3
testCase_Preconditions = 4
testCase_url = 5
testCase_method = 6
testCase_data = 7
testCase_cookie = 8
testCase_theway = 9
testCase_eresult = 10
testCase_runTime = 11
testCase_result = 12
testCase_error = 13
