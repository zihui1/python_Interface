#encoding = utf-8
from . import *
from TestScripts.WriteTestResult import writeTestResult

def dataDriverFun(stepSheetObj,loginname):
    try:
        # # 获取数据源表中是否执行列对象
        # dataIsExecuteColumn = excelObj.getColumn(
        #     stepSheetObj,testCase_isExecute)
        # # 获取数据源表中用例描述
        # emailColumn = excelObj.getColumn(stepSheetObj,testCase_description)
        # 获取测试步骤表中存在数据区域的行数
        stepRowNums = excelObj.getRowsNumber(stepSheetObj)
        # 记录成功执行的数据条数
        successDatas = 0
        # 记录被设置为执行的数据条数
        requiredDatas = 0
        for index in range(2,stepRowNums+1):
            # 获取数据驱动测试步骤表中第index行对象
            rowObj = excelObj.getRow(stepSheetObj,index)
            caseid = rowObj[testCase_id -1].value
            description = rowObj[testCase_description -1].value
            isExecute = rowObj[testCase_isExecute -1].value
            url = rowObj[testCase_url - 1].value
            method = rowObj[testCase_method - 1].value
            data = rowObj[testCase_data - 1].value
            Token = rowObj[testCase_cookie - 1].value
            theway = rowObj[testCase_theway - 1].value
            eresult = rowObj[testCase_eresult - 1].value
            headrs = get_value("Header", "/Config/header.json")
            time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            if isExecute == "y":
                requiredDatas += 1
                log.info(u'执行步骤%s'%(description))
                if Token == "y":
                    getdata = get_value(data,"/Config/shop_data.json")
                    check_json_value(getdata, "accessToken", loginname["accessToken"])
                    check_json_value(getdata, "transDate", time_stamp)
                    check_json_value(getdata, "transNonce", str(uuid.uuid1()))
                    try:
                        respone = request().run_main(method, url, json.dumps(getdata), headrs)
                        if theway == "json":
                            result = handle_result_json(respone.json(),eval(eresult))
                            if result:
                                successDatas += 1
                                writeTestResult(stepSheetObj, rowNo=index, colsNo="testCase", \
                                                testResult="pass")
                                log.info(u'执行步骤%s通过' % (description))
                            else:
                                writeTestResult(stepSheetObj, rowNo=index, colsNo="testCase", \
                                                testResult="faild")
                                log.info(u'执行步骤%s失败' % (description))
                        if theway == "code":
                            if respone.status_code == int(eresult):
                                successDatas += 1
                                writeTestResult(stepSheetObj, rowNo=index, colsNo="testCase", \
                                                testResult="pass")
                                log.info(u'执行步骤%s通过' % (description))
                            else:
                                writeTestResult(stepSheetObj, rowNo=index, colsNo="testCase", \
                                                testResult="faild")
                                log.info(u'执行步骤%s失败' % (description))
                    except Exception as e:
                        log.error(u'执行步骤%s发生异常' % rowObj[testCase_description - 1].value)
                        log.error(traceback.print_exc())
            else:
                # 将不需要执行的数据行的执行时间和执行结果单元格清空
                writeTestResult(stepSheetObj,rowNo=index,colsNo="testCase",\
                                testResult="")
        # log.info(u"共%s条用例，%s条需要被执行，成功执行%s条" \
        #          % (stepRowNums - 1, requiredDatas, successDatas))
        if requiredDatas == successDatas:
            # 只要当成功执行的数据条数等于被设置为需要执行的数据条数，
            # 才表示调用数据驱动的测试用例执行通过
            return 1
        # 表示调用数据驱动的测试用例执行失败
        return None
    except Exception as e:
        raise e