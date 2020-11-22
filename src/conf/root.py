#!/usr/bin/env python
# -*- coding:utf-8 -*-
msh = {
    1: {'cn': '域分隔符', 'en': 'Field Separator'},
    2: {'cn': '编码字符', 'en': 'Encoding Characters'},
    3: {'cn': '发送端软件', 'en': 'Sending Application'},#⭐#
    4: {'cn': '发送端设备', 'en': 'Sending Facility'},
    5: {'cn': '接收端软件', 'en': 'Receiving Application'},
    6: {'cn': '接收端设备', 'en': 'Receiving Facility'},
    7: {'cn': '消息的日期和时间', 'en': 'Date/Time of Message'},
    8: {'cn': '安全', 'en': 'Security'},
    9: {'cn': '消息类型', 'en': 'Message Type'},#⭐#
    10: {'cn': '消息的控制id', 'en': 'Message Control Id'},#⭐#
    11: {'cn': '处理id ', 'en': 'Processing Id'},
    12: {'cn': '版本', 'en': 'idVersion ID'},
    13: {'cn': '序列号', 'en': 'Sequence Number'},
    14: {'cn': '连续指针', 'en': 'Continuation Pointer'},
    15: {'cn': '接收确认消息类型', 'en': 'Accept Acknowledgment Type'},
    16: {'cn': '应用确认消息类型', 'en': 'Application Acknowledgment Type'},
    17: {'cn': '国家码', 'en': 'Country Code'},
    18: {'cn': '字符集', 'en': 'Character Set'},
    19: {'cn': '消息的主要语言', 'en': 'Principal Language Of Message'},
    20: {'cn': '替换字符集处理机制', 'en': 'Alternate Character Set Handling Scheme'},
    21: {'cn': '消息配置文件标识', 'en': 'Message Profile Identifier'},
}

pid = {
    1: {'cn': '集合标识', 'en': 'Set ID - PID'},
    2: {'cn': '病人ID', 'en': 'Patient ID'},
    3: {'cn': '病人标识列表', 'en': 'Patient Identification List',1:'病人ID',4:'授权机构',5:'标识码类型'},#⭐#
    4: {'cn': '替换病人ID', 'en': 'Alternate Patient ID - PID'},
    5: {'cn': '病人姓名', 'en': 'Patient Name',1:'病人姓氏',2:'病人名',3:'病人其它名字',7:'名字类型码'},#⭐#
    6: {'cn': '母亲婚前姓名', 'en': 'Mother’s Maiden Name'},
    7: {'cn': '出生日期', 'en': 'Date/Time of Birth'},#⭐#
    8: {'cn': '性别管理', 'en': 'Administrative Sex','enum':{'M':'男性','F':'女性','U':'未知'}},#⭐#
    19: {'cn': 'SSN号码', 'en': 'SSN Number - Patient'},
}
'''
OBR-4值                                    OBR数据块类型
--------------------------------------------------------
182777000^monitoring of patient^SCT    |   参数
CONTINUOUS WAVEFORM                    |   实时波形
BOUNDED WAVEFORMS                      |   报警相关波形
196616^MDC_EVT_ALARM^MDC               |   报警
'''
obr = {
    1: {'cn': '集合标识', 'en': 'OBR SET id'},
    # OBR-2=MSH-10+MSH-3
    2: {'cn': 'Placer序号', 'en': 'Placer Order Number',1:'实体标识',2:'命名空间标识',3:'通用标识',4:'通用标识类型'},
    # 与OBR-2相同
    3: {'cn': 'Filler序号', 'en': 'Filler Order Number'},
    4: {'cn': '通用服务标识', 'en': 'Universal Service Identifier'},
    5: {'cn': '优先级', 'en': 'Priority - OBR'},
    6: {'cn': '请求时间', 'en': 'Request Date/Time'},
    7: {'cn': '监测时间', 'en': 'Observation Date/Time'},
}

pv1 = {
    1: {'cn': '集合标识', 'en': 'Set ID - PV1'},
    2: {'cn': '病人分类', 'en': 'Patient Class'},
    3: {'cn': '位置信息', 'en': 'Assigned Patient Location',1:"护理区",2:"房间号",3:"床号",4:{1:'机构标识'}},#*#
    7: {'cn': '主治医师', 'en': 'Attending Doctor'},#*#
    8: {'cn': '助理医师', 'en': 'Referring Doctor'},#*#
    9: {'cn': '顾问医师', 'en': 'Consulting Doctor'},
    17: {'cn': '入院医师', 'en': 'Admitting Doctor'},
    19: {'cn': '挂号号码', 'en': 'Visit Number'},
    44: {'cn': '入院日期/时间', 'en': 'Admit Date/Time'},#*#
    51: {'cn': '挂号指示', 'en': 'Visit Indicator'},
}

sft = {
    1: {'cn': '软件提供商', 'en': ''},
    2: {'cn': '软件的合法版本号', 'en': ''},
    3: {'cn': '软件产品名称', 'en': ''},
    4: {'cn': '软件二进制标识', 'en': ''},

}

obx = {
    1: {'cn': '集合标识 ', 'en': "Set ID - OBX"},
    2: {'cn': '数值类型', 'en': "Value Type",'enum':{'NM':'整数小数','SN':'比率','CNE':'枚举值','ST':'字符串'}},
    3: {'cn': '监测参数标识', 'en': "Observation Identifier"},
    4: {'cn': '监测参数', 'en': "Sub-ID Observation Sub-ID"},
    5: {'cn': '监测参数值', 'en': "Observation Value"},
    6: {'cn': '单位', 'en': "Units"},
    7: {'cn': '参考范围', 'en': "Reference Range"},
    8: {'cn': '异常标志', 'en': "Abnormality Flags",'enum':{'DEMO':'演示数据','INV':'无效'}},
    9: {'cn': '概率', 'en': "Probability"},
    10: {'cn': '异常测验实质', 'en': "Nature of Abnormal Test"},
    11: {'cn': '监测结果状态', 'en': "Observation Result Status",'enum':{'F':'有效, 用户已确认','R':'有效, 用户未确认','X':'无效'}},
    12: {'cn': '有效日期', 'en': "Effective Date of Reference Range"},
    13: {'cn': '用户定义检查', 'en': "User Defined Access Check"},
    14: {'cn': '监测日期时间', 'en': "Date/Time of Observation"},
    15: {'cn': '生产者ID', 'en': "Producer's ID"},
    16: {'cn': '责任监测者', 'en': "Responsible Observer"},
    17: {'cn': '监测方法', 'en': "Observation Method"},
    18: {'cn': '设备标识实例', 'en': "Equipment Instance Identifier"},
    19: {'cn': '分析日期时间', 'en': "Date/Time of Analysis"},
    20: {'cn': '监测场所', 'en': "Observation Site"},
}