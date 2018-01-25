#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2018/1/3
import numpy as np
import random
from data_loader import food_info
from nurtition import nutrition


food_dic = food_info()


def get_info(food):
    # print(food[u'能量'], food[u'蛋白质'], food[u'碳水化物'], food[u'脂肪'])
    return np.array([food[u'能量'], food[u'蛋白质'], food[u'碳水化物'], food[u'脂肪']])


def recipe(age, height, weight, gender, activity_level, max_carbohydrate=None, is_diet=None):
    recipe_list = []
    standard_nutrition_list = nutrition(age, height, weight, gender, activity_level)
    energy, protein, carbo, fat = np.array(standard_nutrition_list[:4])
    if max_carbohydrate and max_carbohydrate < carbo:
        carbo = max_carbohydrate
    if is_diet == u'是':
        energy, protein, carbo, fat = 0.8*energy, 0.8*protein, 0.8*carbo, 0.8*fat

    breakfast_dic = food_dic['breakfast']
    breakfast_list = [w for w in breakfast_dic]

    for _ in range(100):
        sample = random.choice(breakfast_list)
        info = breakfast_dic[sample]
        if all([info[u'能量']<energy*0.3, info[u'蛋白质']<protein*0.3, info[u'碳水化物']<carbo*0.3, info[u'脂肪']<fat*0.3]):
            print("The recommand breakfast: %s" % sample)
            recipe_list.append(sample)
            break

    # lunch or dinner
    constraint_lunch = np.array(standard_nutrition_list[:4]) * 0.3
    constraint_dinner = np.array(standard_nutrition_list[:4]) * 0.3

    main_list = food_dic['main'].keys()
    vegetable_list = food_dic['vegetables'].keys()
    meat_list = food_dic['meat'].keys()
    fruit_list = food_dic['fruit'].keys()

    for _ in range(1000):
        sample_main = random.choice(main_list)
        sample_meat = random.choice(meat_list)
        sample_fruit = random.choice(fruit_list)
        sample_vegetable = random.choice(vegetable_list)
        total_nutrition = get_info(food_dic['main'][sample_main]) + get_info(food_dic['vegetables'][sample_vegetable]) + \
                    get_info(food_dic['meat'][sample_meat]) + get_info(food_dic['fruit'][sample_fruit])
        if all(total_nutrition < constraint_lunch):
            print('The recommand lunch: %s %s %s %s' % (sample_main, sample_meat, sample_vegetable, sample_fruit))
            recipe_list.append([sample_main, sample_meat, sample_vegetable, sample_fruit])
            break

    for _ in range(1000):
        sample_main = random.choice(main_list)
        sample_meat = random.choice(meat_list)
        sample_fruit = random.choice(fruit_list)
        sample_vegetable = random.choice(vegetable_list)
        total_nutrition = get_info(food_dic['main'][sample_main]) + get_info(food_dic['vegetables'][sample_vegetable]) + \
                    get_info(food_dic['meat'][sample_meat]) + get_info(food_dic['fruit'][sample_fruit])
        if all(total_nutrition < constraint_dinner):
            print('The recommand dinner: %s %s %s %s' % (sample_main, sample_meat, sample_vegetable, sample_fruit))
            recipe_list.append([sample_main, sample_meat, sample_vegetable, sample_fruit])
            break
    return recipe_list


if __name__ == '__main__':
    # age = raw_input("请输入您的年龄:")
    # height = raw_input("请输入您的身高(cm):")
    # weight = raw_input("请输入您的体重(kg):")
    # gender = raw_input("请输入您的性别(男/女):").decode('utf8')
    # activity_level = raw_input("请输入您的运动量(非常少/较少/较多/非常多):").decode('utf8')
    # max_carbohydrate = raw_input("请输入糖类摄入量最大值(可选):")
    # is_diet = raw_input("请输入是否想减肥(是/否):").decode('utf8')
    # recipe(age, height, weight, gender, activity_level)
    #recipe(30, 175, 60, u'男', u'非常少', 120, u'是')
    recipe(30, 175, 60, u'女', u'较少', is_diet=u'是')

