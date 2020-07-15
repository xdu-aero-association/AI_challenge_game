# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:51:48 2020

@author: asus
"""
import re

class Protocol:
    __init__(self):
        self.person = 0
        #init 需要与数据标签对应
    
    
    def processData(data):
        if('PERSON' and '$/' in data):
            dataLine = re.findall(".*PERSON(.*)$/.*",data)
            dictData= json.loads(dataLine)
            self.person = dictData['people']
            #需要根据模型的json 结果的顺序
        if('GREEN_AND_RED' and '$/' in data):
            dataLine = re.findall(".*PERSON(.*)$/.*",data)
            dictData= json.loads(dataLine)
            #需要根据模型的json 结果的顺序
        if('LOAD_CARD' and '$/' in data):
            dataLine = re.findall(".*PERSON(.*)$/.*",data)
            dictData= json.loads(dataLine)
            
        