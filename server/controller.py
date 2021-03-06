from flask import Blueprint
from flask import render_template, request, jsonify
from server import business
from application import urls

import requests, json

server = Blueprint('server', __name__, template_folder='../application/templates')


@server.route("/demand/model")
def demand_model():
    return render_template('models.html')


@server.route('/add_goods/', methods=['POST'])
def add_goods():
    """
    发布货源，并分析检查点
    :return: dict
    """
    print(request.form.get('openId'), request.form.get('goodsName'))
    openId = request.form.get('openId')
    data = {
        "openId": openId,
        "goodsName": request.form.get('goodsName'),
        "startAddress": request.form.get('startAddress'),
        "endAddress": request.form.get('endAddress'),
        "carryGoodsTime": request.form.get('carryGoodsTime'),
        "carryVolume": request.form.get('carryVolume'),
        "carModel": request.form.get('carModel'),
        "addr": request.form.get('addr'),
        "endDate": request.form.get('endDate')
    }
    isInMydemand = 0
    isInRecommand = 0
    isDemandChecked = 0
    try:
        res = requests.post(urls.url_add_goods, json=data)  # {"retCode":0,"retMsg":"","retData":{"id":"3044"}}
        if res.status_code == 200:
            res = json.loads(res.text)
            if res.get('retCode') == 0:
                retData = res['retData']
                demandId = retData.get('id')

                # 验证需求详情
                print("验证需求详情！")
                retMsg = ""
                if business.check_demand_info(demandId, data).get("retCode") == 0:
                    isDemandChecked = 1
                else:
                    retMsg = business.check_demand_info(demandId, data).get("retMsg")

                # 验证我的需求
                if business.is_in_mydemand(demandId,openId):
                    print("验证我的需求！")
                    isInMydemand = 1

                # 验证需求广场
                if business.is_in_recommand(demandId,openId):
                    print("验证需求广场！")
                    isInRecommand = 1
                return jsonify({"retCode": 0, "retMsg": retMsg,
                                "retData": {"isInMydemand": isInMydemand, "isInRecommand": isInRecommand,
                                            "isDemandChecked": isDemandChecked}})
            else:  # 发布需求时，retCode!=0 的情况
                return jsonify(
                    {"retCode": res.get('retCode'), "retMsg": res.get('retMsg'), "retData": res.get('retData')})
        else:  # 接口请求失败
            return jsonify({"retCode": 90, "retMsg": "请求过程中出现异常", "retData": None})

    except Exception as e:  # 其他异常
        return jsonify({"retCode": 99, "retMsg": str(e), "retData": None})


@server.route('/demand/addCars', methods=["get", "post"])
def add_cars():
    openId = request.form.get('openId')
    data = {
        "openId": request.form.get('openId'),
        "lineData": "[{'from':'南京市','to':'北京市'}]",
        "carNum": request.form.get('carNum'),
        "carModel": "7.6米 公路货车",
        "carryWeight": "10",
        "carryVolume": "40",
        "addr": "上海市青浦区徐德路",
        "lon": 121.265562,
        "lat": 31.192338,
        "endDate": "2018-10-01",
        "contractType": 2,
        "desc": "这里是承运介绍",
        "carImg": "https://wxcx.yunchehome.com/mpw1536216548885.jpg",
        "carPersonImg": "https://wxcx.yunchehome.com/mpw1536216554920.jpg"
    }

    isInMydemand = 0
    isInRecommand = 0
    isDemandChecked = 0
    try:
        res = requests.post(urls.url_add_cars, json=data)
        if res.status_code == 200:
            res = json.loads(res.text)
            if res.get('retCode') == 0:
                retData = res['retData']
                demandId = retData.get('id')

                # 验证需求详情
                print("验证需求详情！")
                retMsg = ""
                if business.check_demand_info(demandId, data).get("retCode") == 0:
                    isDemandChecked = 1
                else:
                    retMsg = business.check_demand_info(demandId, data).get("retMsg")

                # 验证我的需求
                if business.is_in_mydemand(demandId,openId):
                    print("验证我的需求！")
                    isInMydemand = 1

                # 验证需求广场
                if business.is_in_recommand(demandId,openId):
                    print("验证需求广场！")
                    isInRecommand = 1

                return jsonify({"retCode": 0, "retMsg": retMsg,
                                "retData": {"isInMydemand": isInMydemand, "isInRecommand": isInRecommand,
                                            "isDemandChecked": isDemandChecked}})
            return jsonify(
                {"retCode": res.get('retCode'), "retMsg": res.get('retMsg'), "retData": res.get('retData')})

    except Exception as e:
        print(e)
        return jsonify({"retCode": 99, "retMsg": str(e), "retData": None})


@server.route('/demand/addBusiness', methods=["get", "post"])
def add_business():
    openId = request.form.get('openId')
    data = {
        "openId": request.form.get('openId'),
        "companyName": request.form.get('companyName'),
        "merchantsTitle": request.form.get('merchantsTitle'),
        "merchantsArea": "[{\"prov\":\"上海市\",\"city\":\"全域\",\"area\":\"全域\"}]",
        "merchantsStartTime": 1546300800,
        "merchantsEndTime": 1551398400,
        "merchantsType": 2,
        "merchantsTypeTwo": 1,
        "merchantsCharge": request.form.get('merchantsCharge'),
        "phone": request.form.get('phone'),
        "addr": "上海市青浦区华徐公路683号",
        "lon": 121.26601,
        "lat": 31.196965,
        "endDate": "2020-10-01",
        "qualRequire": "【招商】自动发布脚本中的补充说明",
        "businessLicenseImg": request.form.get('businessLicenseImg'),
        "chargeCardImg": request.form.get('chargeCardImg'),
        "url": request.form.get('url')
    }
    isInMydemand = 0
    isInRecommand = 0
    isDemandChecked = 0
    try:
        res = requests.post(urls.url_add_business, json=data)
        if res.status_code == 200:
            res = json.loads(res.text)
            if res.get('retCode') == 0:
                retData = res['retData']
                demandId = retData.get('id')

                # 验证需求详情
                print("验证需求详情！")
                retMsg = ""
                if business.check_demand_info(demandId, data).get("retCode") == 0:
                    isDemandChecked = 1
                else:
                    retMsg = business.check_demand_info(demandId, data).get("retMsg")

                # 验证我的需求
                if business.is_in_mydemand(demandId,openId):
                    print("验证我的需求！")
                    isInMydemand = 1

                # 验证需求广场
                if business.is_in_recommand(demandId,openId):
                    print("验证需求广场！")
                    isInRecommand = 1

                return jsonify({"retCode": 0, "retMsg": retMsg,
                                "retData": {"isInMydemand": isInMydemand, "isInRecommand": isInRecommand,
                                            "isDemandChecked": isDemandChecked}})
            return jsonify(
                {"retCode": res.get('retCode'), "retMsg": res.get('retMsg'), "retData": res.get('retData')})

    except Exception as e:
        print(e)
        return jsonify({"retCode": 99, "retMsg": str(e), "retData": None})


@server.route('/demand/addCarSell', methods=["get", "post"])
def add_carsell():
    openId = request.form.get('openId')
    data = {
        "openId": request.form.get('openId'),
        "addr": "上海市青浦区华徐公路683号",
        "lon": 121.26601,
        "lat": 31.196965,
        "endDate": "2018-10-10",
        "carSort": request.form.get('carSort'),
        "driveForm": 9,
        "carBrandsId": "39",
        "carSeriesId": "46",
        "maxPower": "300",
        "emissionStand": request.form.get('emissionStand'),
        "drivingLiceDate": "",
        "kilometers": "",
        "shellPrice": request.form.get('shellPrice'),
        "carImg": request.form.get('carImg'),
        "drivingRoomImg": request.form.get('drivingRoomImg'),
        "chassisImg": request.form.get('chassisImg'),
        "desc": request.form.get('desc')
    }
    isInMydemand = 0
    isInRecommand = 0
    isDemandChecked = 0
    try:
        res = requests.post(urls.url_add_carsell, json=data)
        if res.status_code == 200:
            res = json.loads(res.text)
            if res.get('retCode') == 0:
                retData = res['retData']
                demandId = retData.get('id')

                print("验证需求详情！")
                if business.check_demand_info(demandId, data).get("retCode") == 0:
                    isDemandChecked = 1
                else:
                    retMsg = business.check_demand_info(demandId, data).get("retMsg")

                # 验证我的需求
                if business.is_in_mydemand(demandId,openId):
                    print("验证我的需求！")
                    isInMydemand = 1

                # 验证需求广场
                if business.is_in_recommand(demandId,openId):
                    print("验证需求广场！")
                    isInRecommand = 1

                return jsonify({"retCode": 0, "retMsg": retMsg,
                                "retData": {"isInMydemand": isInMydemand, "isInRecommand": isInRecommand,
                                            "isDemandChecked": isDemandChecked}})
            return jsonify(
                {"retCode": res.get('retCode'), "retMsg": res.get('retMsg'), "retData": res.get('retData')})

    except Exception as e:
        print(e)
        return jsonify({"retCode": 99, "retMsg": str(e), "retData": None})


@server.route('/demand/addOtherDemand', methods=["get", "post"])
def add_other():
    # print("openId:%s" % request.get_json(force=True)['openId'])
    # print(request.get_json(force=True)['info']['type'])
    # print(type(request.get_json(force=True)['info']))
    openId = request.get_json(force=True)['openId']
    data = {
        "openId": openId,
        "info": json.dumps(request.get_json(force=True)['info'])
    }

    print("data:%s" % data)
    isInMydemand = 0
    isInRecommand = 0
    isDemandChecked = 0
    try:
        res = requests.post(urls.url_add_other, data)
        print(res.text)
        if res.status_code != 200:
            return jsonify(
                {"retCode": res.get('retCode'), "retMsg": "status code != 200", "retData": res.get('retData')})
        res = json.loads(res.text)

        if res.get('retCode') != 0:
            return jsonify(
                {"retCode": res.get('retCode'), "retMsg": res.get('retMsg'), "retData": res.get('retData')})

        retData = res['retData']
        demandId = retData.get('id')

        retMsg = ""
        print("验证需求详情！")
        if business.check_demand_info(demandId, data).get("retCode") == 0:
            isDemandChecked = 1
        else:
            retMsg = business.check_demand_info(demandId, data).get("retMsg")

        # 验证我的需求
        print("验证我的需求！")
        if business.is_in_mydemand(demandId, openId):
            isInMydemand = 1

        # 验证需求广场
        print("验证需求广场！")
        if business.is_in_recommand(demandId, openId):
            isInRecommand = 1

        return jsonify({"retCode": 0, "retMsg": retMsg,
                        "retData": {"isInMydemand": isInMydemand, "isInRecommand": isInRecommand,
                                    "isDemandChecked": isDemandChecked}})

    except Exception as e:
        print("Exception:",e)
        return jsonify({"retCode": 99, "retMsg": str(e), "retData": None})


@server.route('/getOpenIds', methods=["get", "post"])
def getOpenIds():
    return jsonify([{
        "id": "o94HS5PrLEd6AeyLRM5XimFX90tU",
        "text": "o94HS5PrLEd6AeyLRM5XimFX90tU",
        "selected": True
    }, {
        "id": "o94HS5Amxfcwn9pgj-fvByTp70Do",
        "text": "o94HS5Amxfcwn9pgj-fvByTp70Do"
    }, {
        "id": "o94HS5ODKlPjrGety5Ocz18yGnz4",
        "text": "o94HS5ODKlPjrGety5Ocz18yGnz4"
    }])


@server.route('/editMobileAuth', methods=['post'])
def edit_mobileAuth():
    uid = request.form.get('uid')
    type = request.form.get('type')
    if not uid or not type:
        return jsonify({"retCode": -1, "retMsg": "uid 或 type不能为空"})

    from application.utils import mysqlUtil

    # sql = "SELECT * FROM user_card where mobile = %s"
    sql = "UPDATE user_card set isMobileAuth=%s where uid = %s"
    db = mysqlUtil.MysqlCommand(host='192.168.40.67', user='dbdev', password='123456', database='api_business_card',
                                charset='utf8')

    # res = db.runQuery(sql,"18521035133")
    if db.runCud(sql, (type, uid)):
        return jsonify({"retCode": 0, "retMsg": "success"})
    db.close()
    return jsonify({"retCode": 2, "retMsg": "error"})


@server.route('/getUser',methods=['post','get'])
def getUser():
    uid = request.args.get("uid")

    # 判断uid是否为空
    if not uid:
        return  jsonify({"retCode":11,"retMsg":"uid不能为空！","retData":""})

    # 判断uid是否存在
    if uid != "2020":
        return jsonify({"retCode": 12, "retMsg": "uid不存在！", "retData": ""})

    return jsonify({"retCode":0,"retMsg":"success","retData":"xiaofang"})
