#encoding = utf-8
from . import *
from . import CreateContacts
from TestScripts.WriteTestResult import writeTestResult

def TestSendMailAndCreateContacts():
    try:
        # 根据Excel文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByName(u'APP')
        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet,testStep_isExecute)
        # 记录执行成功的测试用例个数
        successfulCase = 0
        # 记录需要执行的用例个数
        requiredCase =0
        for idx,i in enumerate(isExecuteColumn[1:]):
            # 因为用例sheet中第一行为标题行，无须执行
            caseName = excelObj.getCellOfValue(caseSheet,rowNo=idx+2,\
                                               colsNo=testStep_testCaseName)
            # 循环遍历“测试用例”表中的测试用例，执行被设置为执行的用例
            if i.value.lower() == "y":
                requiredCase +=1
                # 获取测试用例表中，第idx+1行中
                # 获取测试用例列中，第idx+1行中执行用例的步骤sheet名
                stepSheetName = excelObj.getCellOfValue(\
                    caseSheet,rowNo=idx+2,colsNo=testStep_testStepSheetName)
                log.info('----------'+stepSheetName)
                stepSheetObj = excelObj.getSheetByName(stepSheetName)
                loginname = login(stepSheetName)
                result = CreateContacts.dataDriverFun(stepSheetObj,loginname)
                if result:
                    log.info(u'用例%s执行成功' % (caseName))
                    successfulCase += 1
                    writeTestResult(caseSheet, rowNo=idx + 2, \
                                    colsNo="caseStep", testResult="pass")
                else:
                    log.info(u'用例%s执行失败' % (caseName))
                    writeTestResult(caseSheet, rowNo=idx + 2, colsNo="caseStep", testResult="faild")
        log.info(u"共%s条用例，%s条需要被执行，成功执行%s条"\
                 %(len(isExecuteColumn)-1,requiredCase,successfulCase))
    except Exception as e:
        log.info("出现异常"+traceback.format_exc())
