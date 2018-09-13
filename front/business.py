import requests, json
from front import urls

openId = "o94HS5PrLEd6AeyLRM5XimFX90tU"


def is_in_mydemand(demandId):
    flag = False
    data = {
        "page": 1,
        "lon": 121.266042,
        "lat": 31.196979,
        "openId": openId
    }
    res = requests.post(urls.url_userDemand, json=data)
    # {"retCode":0,"retMsg":"","retData":{"list":[{"id":"3043","demandId":"3043","goodsName":"\u624b\u673a","startAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u534e\u5f90\u516c\u8def888\u53f7","endAddress":"\u5317\u4eac\u5e02\u6d77\u6dc0\u533a","startAddressLon":0,"startAddressLat":0,"endAddressLon":"0","endAddressLat":"0","carryGoodsTime":"1546255800","carryWeight":0,"carryVolume":22,"carryLong":"0","carryHeight":"0","carryWidth":"0","carryNum":"0","carModel":"1.8\u7c73 \u534a\u6302\u7275\u5f15\u8f66","carType":"0","isTailPlate":"0","isCarry":"0","isCarpool":"0","payType":"0","supplyType":"0","goodsNum":"0","transportMoney":"-1","createTime":"1535952918","title":"\u624b\u673a","desc":"","endDate":"1607990400","status":"1","updateTime":"1535952918","uid":"8473","view":"0","url":"","type":"1","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u53cc\u8054\u8def88\u53f7","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":0,"lat":0,"reason":"","deTime":"2018-09-03","strCarType":"","strIsTailPlate":"","strIsCarry":"","strIsCarpool":"","strPayType":"","strSupplyType":"","isEnd":0,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"3042","demandId":"3042","goodsName":"\u624b\u673a","startAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u534e\u5f90\u516c\u8def888\u53f7","endAddress":"\u5317\u4eac\u5e02\u6d77\u6dc0\u533a","startAddressLon":0,"startAddressLat":0,"endAddressLon":"0","endAddressLat":"0","carryGoodsTime":"1546255800","carryWeight":0,"carryVolume":22,"carryLong":"0","carryHeight":"0","carryWidth":"0","carryNum":"0","carModel":"1.8\u7c73 \u534a\u6302\u7275\u5f15\u8f66","carType":"0","isTailPlate":"0","isCarry":"0","isCarpool":"0","payType":"0","supplyType":"0","goodsNum":"0","transportMoney":"-1","createTime":"1535952698","title":"\u624b\u673a","desc":"","endDate":"1607990400","status":"1","updateTime":"1535952698","uid":"8473","view":"0","url":"","type":"1","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u53cc\u8054\u8def88\u53f7","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":0,"lat":0,"reason":"","deTime":"2018-09-03","strCarType":"","strIsTailPlate":"","strIsCarry":"","strIsCarpool":"","strPayType":"","strSupplyType":"","isEnd":0,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"3038","demandId":"3038","goodsName":"\u624b\u673a","startAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u534e\u5f90\u516c\u8def888\u53f7","endAddress":"\u5317\u4eac\u5e02\u6d77\u6dc0\u533a","startAddressLon":0,"startAddressLat":0,"endAddressLon":"0","endAddressLat":"0","carryGoodsTime":"1546255800","carryWeight":0,"carryVolume":22,"carryLong":"0","carryHeight":"0","carryWidth":"0","carryNum":"0","carModel":"1.8\u7c73 \u534a\u6302\u7275\u5f15\u8f66","carType":"0","isTailPlate":"0","isCarry":"0","isCarpool":"0","payType":"0","supplyType":"0","goodsNum":"0","transportMoney":"-1","createTime":"1535696808","title":"\u624b\u673a","desc":"","endDate":"1607990400","status":"1","updateTime":"1535696808","uid":"8473","view":"0","url":"","type":"1","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u53cc\u8054\u8def88\u53f7","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":0,"lat":0,"reason":"","deTime":"2018-08-31","strCarType":"","strIsTailPlate":"","strIsCarry":"","strIsCarpool":"","strPayType":"","strSupplyType":"","isEnd":0,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"3033","demandId":"3033","goodsName":"\u8349\u8393","startAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","endAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","startAddressLon":121.271685,"startAddressLat":31.19573,"endAddressLon":"1212716850","endAddressLat":"311957300","carryGoodsTime":"1535715000","carryWeight":0,"carryVolume":22,"carryLong":"0","carryHeight":"0","carryWidth":"0","carryNum":"0","carModel":"1.8\u7c73 \u534a\u6302\u7275\u5f15\u8f66","carType":"0","isTailPlate":"0","isCarry":"0","isCarpool":"0","payType":"1","supplyType":"1","goodsNum":"10","transportMoney":"200000","createTime":"1535685791","title":"\u8349\u8393","desc":"\u8fd9\u91cc\u662f\u5907\u6ce8","endDate":"1536969600","status":"1","updateTime":"1535685791","uid":"8473","view":"1","url":"https:\/\/wxcx.yunchehome.com\/mpw1535685780654.jpg;https:\/\/wxcx.yunchehome.com\/mpw1535685785862.jpg","type":"1","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","secreport":"6","top":"0","topStartTime":"0","topEndTime":"0","lon":121.271685,"lat":31.19573,"reason":"","deTime":"2018-08-31","strCarType":"","strIsTailPlate":"","strIsCarry":"","strIsCarpool":"","strPayType":"\u53d1\u8d27\u4eba\u4ed8","strSupplyType":"\u5355\u6b21\u8fd0\u8f93","isEnd":0,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"3032","demandId":"3032","goodsName":"\u7535\u5b50\u624b\u8868","startAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","endAddress":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","startAddressLon":121.271685,"startAddressLat":31.19573,"endAddressLon":"1212716850","endAddressLat":"311957300","carryGoodsTime":"1535749200","carryWeight":10,"carryVolume":0,"carryLong":"0","carryHeight":"0","carryWidth":"0","carryNum":"0","carModel":"4.2\u7c73 \u534a\u6302\u7275\u5f15\u8f66","carType":"0","isTailPlate":"0","isCarry":"0","isCarpool":"0","payType":"0","supplyType":"0","goodsNum":"0","transportMoney":"0","createTime":"1535684907","title":"\u7535\u5b50\u624b\u8868","desc":"","endDate":"1536969600","status":"1","updateTime":"1535700576","uid":"8473","view":"2","url":"","type":"1","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u6148\u6c11\u8def","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":121.271685,"lat":31.19573,"reason":"","deTime":"2018-08-31","strCarType":"","strIsTailPlate":"","strIsCarry":"","strIsCarpool":"","strPayType":"","strSupplyType":"","isEnd":0,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"2867","title":"\u6c42\u804c\u610f\u5411\u5f88\u5f3a\u70c8\uff011","desc":"\u56fd\u6709\u5927\u4f01\u4e1a\uff0c\u671d\u4e5d\u665a\u4e94\uff0c\u53cc\u500d\u5de5\u8d44\u3002","endDate":"1534780800","status":"1","createTime":"1532919884","updateTime":"1533537898","uid":"8473","view":"21","url":"https:\/\/wxcx.yunchehome.com\/mpw1533274023214.jpg","type":"10","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5317\u9752\u516c\u8def","secreport":"0","top":"0","topStartTime":"1533513600","topEndTime":"1533600000","lon":121.2598,"lat":31.2025,"reason":"sdsds","demandId":"2867","deTime":"2018-07-30","isEnd":1,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"2866","demandId":"2866","companyName":"\u4e0a\u6d77\u9a7c\u76ca\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","companyDesc":"","address":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5317\u9752\u516c\u8def","businessArea":"2","merchantsTitle":"\u7f8e\u7684\u7a7a\u8c03\u62db\u7701\u7ea7\u4ee3\u7406\u516c\u53f8\uff0c\u4e0a\u6d77\u96f7\u52b1\u6295\u8d44\uff0c\u6b22\u8fce\u6b22\u8fce\u3002","merchantsArea":"[{\"prov\":\"\u4e0a\u6d77\u5e02\",\"city\":\"\u4e0a\u6d77\u5e02\",\"area\":\"\u9752\u6d66\u533a\"},{\"prov\":\"\u6c5f\u82cf\u7701\",\"city\":\"\u5168\u57df\",\"area\":\"\u5168\u57df\"}]","merchantsStartTime":"1535587200","merchantsEndTime":"1548979200","merchantsType":"1","merchantsTypeTwo":"0","qualRequire":"\u4e00\u5b9a\u8981\u6709\u5b9e\u529b\u624d\u53ef\u4ee5","otherDesc":"","merchantsCharge":"\u73a9\u5bb6\u73a9\u5bb6","phone":"18521035133","businessLicenseImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266758569.jpg","chargeCardImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266763620.jpg","createTime":"1532919884","title":"","desc":"","endDate":"1534521600","status":"1","updateTime":"1533266873","uid":"8473","view":"32","url":"https:\/\/wxcx.yunchehome.com\/mpw1533266771811.jpg","type":"9","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5317\u9752\u516c\u8def","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":121.25847,"lat":31.20229,"reason":"","deTime":"2018-07-30","strBusinessArea":"\u5168\u56fd","strMerchantsType":"\u5feb\u8fd0","isEnd":1,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":2},{"id":"2869","title":"\u672c\u516c\u53f8\u957f\u671f\u63d0\u4f9b\u7535\u98ce\u6247\uff0c\u6b22\u8fce\u6d3d\u8c08","desc":"\u590f\u5b63\u5b9d\u5b9d\u795b\u75f1\u5b50\u7684\u5b9e\u7528\u65b9\u6cd5[\u73ab\u7470]\n\n\u82e6\u74dc\u5177\u6709\u6e05\u70ed\u6d88\u6691\u3001\u517b\u8840\u76ca\u6c14\u3001\u8865\u80be\u5065\u813e\u3001\u6ecb\u809d\u660e\u76ee\u7684\u4f5c\u7528\uff0c\u5bf9\u4e8e\u6cbb\u7597\u75f1\u5b50\u6548\u679c\u5f88\u597d\u3002\u56e0\u6b64\uff0c\u5988\u5988\u53ef\u4ee5\u7528\u82e6\u74dc\u6765\u7ed9\u5b9d\u5b9d\u64e6\u62ed\u8eab\u4e0a\u957f\u75f1\u5b50\u5904\uff0c\u80fd\u6709\u6548\u6e05\u9664\u75f1\u5b50\uff0c\u8981\u7528\u5230\u7684\u662f\u82e6\u74dc\u7684\u5185\u82af\u3002\n\u5c06\u82e6\u74dc\u5bf9\u534a\u5207\u5f00\uff0c\u5c06\u5185\u90e8\u7684\u767d\u74e4\u8fde\u82e6\u74dc\u7c7d\u4e00\u8d77\u6316\u51fa\uff0c\u653e\u5165\u9505\u4e2d\uff0c\u52a0\u5165\u6e05\u6c34\u3002","endDate":"1534521600","status":"1","createTime":"1533275332","updateTime":"1533275332","uid":"8473","view":"15","url":"","type":"8","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5f90\u9f99\u8def","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":121.27145,"lat":31.195312,"reason":"","demandId":"2869","deTime":"2018-08-03","isEnd":1,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"2865","demandId":"2865","carSort":"1","carBrandsId":"30","carSeriesId":"31","driveForm":"0","drivingLiceDate":"0","kilometers":"0","maxPower":"0","emissionStand":"2","shellPrice":"888000000","drivingRoomImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266603540.jpg","carImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266598193.jpg","chassisImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266618516.jpg","createTime":"1532919884","title":"","desc":"","endDate":"1534521600","status":"1","updateTime":"1533281225","uid":"8473","view":"35","url":"https:\/\/wxcx.yunchehome.com\/mpw1533266598193.jpg;https:\/\/wxcx.yunchehome.com\/mpw1533266603540.jpg;https:\/\/wxcx.yunchehome.com\/mpw1533266618516.jpg","type":"7","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5f90\u6cfe\u9547\u6f58\u9f99\u6751280\u53f7\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u57f9\u82f1\u6c11\u529e\u5c0f\u5b66\u9644\u8fd1","secreport":"0","top":"1","topStartTime":"1534485780","topEndTime":"1537142400","lon":121.27472,"lat":31.190786,"reason":"drrr","deTime":"2018-07-30","strCarBrands":"\u5317\u6c7d\u5a01\u65fa","strCarSeries":"\u5a01\u65fa","strCarSort":"\u65b0\u8f66","strDriveForm":"","strEmissionStand":"\u56fd\u4e09","isEnd":1,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0},{"id":"2863","demandId":"2863","carSort":"1","carBrandsId":"1","carSeriesId":"2","driveForm":"1","drivingLiceDate":"0","kilometers":"0","maxPower":"200","emissionStand":"1","shellPrice":"66000000","drivingRoomImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266072938.jpg","carImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266068190.jpg","chassisImg":"https:\/\/wxcx.yunchehome.com\/mpw1533266077929.jpg","createTime":"1532919884","title":"","desc":"\u5f88\u6b63\u5e38","endDate":"1534521600","status":"1","updateTime":"1533266083","uid":"8473","view":"21","url":"https:\/\/wxcx.yunchehome.com\/mpw1533266068190.jpg;https:\/\/wxcx.yunchehome.com\/mpw1533266072938.jpg;https:\/\/wxcx.yunchehome.com\/mpw1533266077929.jpg","type":"7","addr":"\u4e0a\u6d77\u5e02\u9752\u6d66\u533a\u5317\u9752\u516c\u8def","secreport":"0","top":"0","topStartTime":"0","topEndTime":"0","lon":121.2598,"lat":31.2025,"reason":"","deTime":"2018-07-30","strCarBrands":"\u5317\u4eac\u724c","strCarSeries":"3036\u7cfb\u5217","strCarSort":"\u65b0\u8f66","strDriveForm":"4X2","strEmissionStand":"\u56fd\u4e8c","isEnd":1,"cardType":"14","strCardType":"\u7269\u6d41\u79d1\u6280\u4eba","grand":"0","pic":"https:\/\/wx.qlogo.cn\/mmopen\/vi_32\/PiajxSqBRaELUDxs6jR3kicJDloe9icbM9dZTosx8VBcbrOULQRf2GFjBUAQycBe97ibZiciaMwQBBICjYJtIvLkTRIw\/132","job":"\u9996\u5e2d\u4f53\u9a8c\u5b98","name":"\u804c\u4e1a\u89c4\u5212","corpId":"2930","level":3,"bpic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4b.png","spic":"https:\/\/wxcx.yunchehome.com\/h5\/image\/wx\/v3-4s.png","standard":"10000","usertitle":"\u79e9\u5e8f\u5c0f\u767d\u94f6","corpName":"\u4e0a\u6d77\u96f7\u51cc\u4fe1\u606f\u79d1\u6280\u6709\u9650\u516c\u53f8","corpCert":"2","cardId":"9203","isLike":0,"likeNum":0}],"count":36,"invalidCount":31}}
    if res.status_code == 200:
        res = json.loads(res.text)
        if len(res['retData']['list']):
            for d in res['retData']['list']:
                if demandId == d['demandId']:
                    flag = True
                    break
    return flag


def is_in_recommand(demandId):
    flag = False
    data = {
        "page": 1,
        "lon": 121.265562,
        "lat": 31.192338,
        "openId": openId
    }
    res = requests.post(urls.url_recommand, json=data)
    if res.status_code == 200:
        res = json.loads(res.text)
        if res.get('retCode') == 0 and len(res.get('retData').get('list')) > 0:
            for d in res.get('retData').get('list'):
                if demandId == d.get('demandId'):
                    flag = True
                    break
    return flag


def check_goods_info(demandId, params):
    """
    判断请求参数 和 返回参数是否一致
    :param demandId: 需求id
    :param params: 请求时的参数
    :return:
    """
    flag = False
    data = {
        "openId": params.get('openId'),
        "id": demandId
    }
    res = requests.post(urls.url_demandInfo, json=data)
    if res.status_code == 200:
        res = json.loads(res.text)
        if res['retCode'] == 0 and res['retData'].get('detail'):
            detail = res['retData']['detail']
            flag = True if params['goodsName'] == detail['goodsName'] else False

    return flag


def check_car_info(demandId, params):
    """
    判断请求参数 和 返回参数是否一致
    :param demandId: 需求id
    :param params: 请求时的参数
    :return:
    """
    retCode = -1
    data = {
        "openId": params.get('openId'),
        "id": demandId
    }
    res = requests.post(urls.url_demandInfo, json=data)
    if res.status_code == 200:
        res = json.loads(res.text)
        if res['retCode'] == 0 and res['retData'].get('detail'):
            detail = res['retData']['detail']
            flag_carNum = True if params['carNum'] == detail['carNum'] else "except {} but get {}".format(
                params['carNum'], detail['carNum'])
            flag_carModel = True if params['carModel'] == detail['carModel'] else "except {} but get {}".format(
                params['carModel'], detail['carModel'])
            flag_addr = True if params['addr'] == detail['addr'] else False
            flag_carryWeight = True if params['carryWeight'] == detail['carryWeight'] else False
            flag_carryVolume = True if params['carryVolume'] == detail['carryVolume'] else False
            flag_endDate = True if params['endDate'] == detail['endDate'] else "except {} but get {}".format(
                params['endDate'], detail['endDate'])

            if flag_carNum and flag_carModel and flag_addr and flag_carryWeight and flag_carryVolume:
                retCode = 0

            return {"retCode": retCode, "retData": {"carNum": flag_carNum, "carModel": flag_carModel, "addr": flag_addr,
                                                    "carryWeight": flag_carryWeight, "carryVolume": flag_carryVolume,
                                                    "flag_endDate": flag_endDate}}
        return {"retCode": retCode}

    return {"retCode": retCode}


def check_business_info(demandId, reqParams):
    """
    判断请求参数 和 返回参数是否一致
    :param demandId: 需求id
    :param reqParams: 请求时的参数
    :return:
    """
    retCode = 0
    data = {
        "openId": reqParams.get('openId'),
        "id": demandId
    }
    res = requests.post(urls.url_demandInfo, json=data)
    if res.status_code == 200:
        res = json.loads(res.text)
        print("business status code == 200")
        if res['retCode'] == 0 and res['retData'].get('detail'):
            print("retcode == 0")
            resDetail = res['retData'].get('detail')
            errMsg = []
            for k in reqParams.keys() & resDetail.keys():
                # dict key==key
                if str(reqParams[k]) != str(resDetail[k]):
                    retCode = -1
                    errMsg.append("except {}:{},but get:{}".format(k, reqParams[k], resDetail[k]))
                    print(" key:{}, except:{}, but get:{}".format(k, reqParams[k], resDetail[k]))
                    # break
                else:  # key1 != key2 ,跳过，不处理
                    continue
            return {"retCode": retCode, "retMsg": errMsg}

        else:
            retCode = 99
            retMsg = "retCode:{},retData:{}".format(res['retCode'], res['retData'])
            return {"retCode": retCode, "retMsg": retMsg}

    return {"retCode": 500, "retMsg": "some error occours in request!"}



def check_carsell(demandId, reqParams):
    """
    判断请求参数 和 返回参数是否一致
    :param demandId: 需求id
    :param reqParams: 请求时的参数
    :return:
    """
    retCode = 0
    data = {
        "openId": reqParams.get('openId'),
        "id": demandId
    }
    res = requests.post(urls.url_demandInfo, json=data)
    if res.status_code == 200:
        res = json.loads(res.text)
        print("business status code == 200")
        if res['retCode'] == 0 and res['retData'].get('detail'):
            print("retcode == 0")
            resDetail = res['retData'].get('detail')
            errMsg = []
            for k in reqParams.keys() & resDetail.keys():
                # dict key==key
                if str(reqParams[k]) != str(resDetail[k]):
                    retCode = -1
                    errMsg.append("{} should be:({}),but get:({})".format(k, reqParams[k], resDetail[k]))
                    print(" key:{}, except:{}, but get:{}".format(k, reqParams[k], resDetail[k]))
                    # break
                else:  # key1 != key2 ,跳过，不处理
                    continue
            return {"retCode": retCode, "retMsg": errMsg}

        else:
            retCode = 99
            retMsg = "retCode:{},retData:{}".format(res['retCode'], res['retData'])
            return {"retCode": retCode, "retMsg": retMsg}

    return {"retCode": 500, "retMsg": "some error occours in request!"}


if __name__ == '__main__':
    check_goods_info(openId, 3074)
