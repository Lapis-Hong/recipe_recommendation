#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2017/12/22
import csv
import sys
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf8')


def food_info():
    with open('food_info.csv') as f:
        reader = csv.reader(f)
        head_row = reader.next()
        head_row = [w.decode('gbk') for w in head_row]  # to unicode
        nutrient_name = head_row[2:]
        food_dic = defaultdict(dict)
        for line in reader:
            category = line[0]
            name = line[1].decode('gbk')
            nutrient_value = []
            for value in line[2:]:  # ['1.3','2','','4.5']
                if value:
                    try:
                        nutrient_value.append(float(value))
                    except ValueError:
                        nutrient_value.append(value)
                else:
                    nutrient_value.append(0)
            if category:
                food_dic[category][name] = dict(zip(nutrient_name, nutrient_value))
        # print(food_dic['main'][u'大黄米（黍）'][u'能量'])
    return food_dic




