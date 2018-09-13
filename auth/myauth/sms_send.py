# -*- coding: utf-8 -*-
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT
from random import randint

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12

"""
try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient('LTAINLu2ng99Jg7c', '1eAUfKDLlTRu2I65FQ9snu2kfBHTQ1', REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def send_sms(phone_numbers, template_param=None, sign_name="Django项目", template_code="SMS_144151952"):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(uuid.uuid1())

    # 短信签名
    smsRequest.set_SignName(sign_name)

    # 数据提交方式
    smsRequest.set_method(MT.POST)

    # 数据提交格式
    smsRequest.set_accept_format(FT.JSON)

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse



if __name__ == '__main__':
    __business_id = uuid.uuid1()
    #print(__business_id)
    #params = "{\"code\":\"12345\",\"product\":\"云通信\"}"
    params = u'{"code":"%d"}' % randint(100000, 999999)
    print(send_sms("18813051611", params, "Django项目", "SMS_144151952"))
   
    
    

