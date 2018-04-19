# coding=utf8
import numpy as np


def EER(age, weight, height, gender, activity_level):
    if gender == u'男':
        if activity_level == u'非常少':
            PA = 1
        elif activity_level == u'较少':
            PA = 1.11
        elif activity_level == u'较多':
            PA = 1.25
        elif activity_level == u'非常多':
            PA = 1.48
        else:
            raise ValueError('运动量%s不符合，请输入正确的运动量' % activity_level)

        if 3 < age <= 8:
            EER = 88.5 - 61.9 * float(age) + PA * (26.7 * float(weight) + 9.03 * float(height)) + 20
        elif 8 < age <= 18:
            EER = 88.5 - 61.9 * float(age) + PA * (26.7 * float(weight) + 9.03 * float(height)) + 25
        elif age > 18:
            EER = 662 - 9.53 * float(age) + PA * (15.91 * float(weight) + 5.396 * float(height))
        else:
            raise ValueError('请输入正确的年龄')

    elif gender == u'女':
        if activity_level == u'非常少':
            PA = 1
        elif activity_level == u'较少':
            PA = 1.12
        elif activity_level == u'较多':
            PA = 1.27
        elif activity_level == u'非常多':
            PA = 1.45
        else:
            raise ValueError('请输入正确的运动量')

        if 3 < age <= 8:
            EER = 135.3 - 30.8 * float(age) + PA * (10.0 * float(weight) + 9.34 * float(height)) + 20
        elif 8 < age <= 18:
            EER = 135.3 - 30.8 * float(age) + PA * (10.0 * float(weight) + 9.34 * float(height)) + 25
        elif age > 18:
            EER = 354 - 6.91 * float(age) + PA * (9.36 * float(weight) + 7.26 * float(height))
        else:
            raise ValueError('请输入正确的年龄')
    else:
        raise ValueError('请输入正确的性别（男/女）')

    return EER


def nutrition(age, weight, height, gender, activity_level):
    aaEER = EER(age, weight, height, gender, activity_level)
    if gender == u'男':
        if age <= 17:
            age_list = [4, 8, 9, 13, 14, 17]
            EER_lsit = [1300, 1700, 1700, 1900, 2100, 3200]
            real_age = np.interp(aaEER, EER_lsit, age_list)  # One-dimensional linear interpolation.
        else:
            age_list = [18, 19, 30, 31, 50, 51]
            EER_lsit = [3100, 3100, 2300, 2100, 2000, 2000]
            real_age = np.interp(aaEER, EER_lsit, age_list)
    elif gender == u'女':
        if age <= 36:
            age_list = [4, 8, 9, 13, 14, 18, 19, 30, 31, 36]
            EER_lsit = [1100, 1400, 1400, 1700, 1700, 1900, 1900, 2100, 2100, 2200]
            real_age = np.interp(aaEER, EER_lsit, age_list)
        else:
            age_list = [36, 41, 46, 50, 51, 60]
            EER_lsit = [2200, 2100, 2000, 1900, 1900, 1600]
            real_age = np.interp(aaEER, EER_lsit, age_list)
    else:
        raise ValueError

    if gender == u'男':
        if 3 < real_age <= 8:
            Macronutrients = {'Protein,g': '13', 'Protein,kcal': '12.5', 'Carbonhydrate,g': '130',
                              'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '14', 'AddedSugars,kcal': '<10%',
                              'TotalFat,kcal': '35', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '7',
                              'LinolenicAcid,g': '0.7'}
            Minerals = {'Calcium,mg': '700', 'Iron,mg': '7', 'Magnesium,mg': '80', 'Phosphorus,mg': '460',
                        'Potassium,mg': '3000', 'Sodium,mg': '1500', 'Zinc,mg': '3', 'Copper,mcg': '340',
                        'Manganese,mg': '1.2', 'Selenium,mcg': '20'}
            Vitamins = {'Vitamin A, mg RAE': '300', 'Vitamin E,mg AT': '6', 'Vitamin D, IU': '600', 'Vitamin C, mg': '15',
                        'Thiamin, mg': '0.5', 'Riboflavin, mg': '0.5', 'Niacin, mg': '6', 'Vitamin B6, mg': '0.5',
                        'Vitamin B12, mcg': '0.9', 'Choline, mg': '200', 'Vitamin K, mcg': '30', 'Folate, mcg DFE': '150'}
        elif 8 < real_age <= 13:
            Macronutrients = {'Protein,g': '34', 'Protein,kcal': '20', 'Carbonhydrate,g': '130',
                          'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '25.2', 'AddedSugars,kcal': '<10%',
                          'TotalFat,kcal': '30', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '12',
                          'LinolenicAcid,g': '1.2'}
            Minerals = {'Calcium,mg': '1300', 'Iron,mg': '8', 'Magnesium,mg': '240', 'Phosphorus,mg': '1250',
                'Potassium,mg': '4500', 'Sodium,mg': '2200', 'Zinc,mg': '8', 'Copper,mcg': '700', 'Manganese,mg': '1.9',
                'Selenium,mcg': '40'}
            Vitamins = {'Vitamin A, mg RAE': '600', 'Vitamin E,mg AT': '11', 'Vitamin D, IU': '600', 'Vitamin C, mg': '45',
                'Thiamin, mg': '0.9', 'Riboflavin, mg': '0.9', 'Niacin, mg': '12', 'Vitamin B6, mg': '1',
                'Vitamin B12, mcg': '1.8', 'Choline, mg': '250', 'Vitamin K, mcg': '55', 'Folate, mcg DFE': '200'}
        elif 13 < real_age <= 18:
            Macronutrients = {'Protein,g': '52', 'Protein,kcal': '20', 'Carbonhydrate,g': '130', 'Carbonhydrate,kcal': '55',
                  'DietaryFiber,g': '30.8', 'AddedSugars,kcal': '<10%', 'TotalFat,kcal': '30',
                  'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '16', 'LinolenicAcid,g': '1.6'}
            Minerals = {'Calcium,mg': '1300', 'Iron,mg': '11', 'Magnesium,mg': '410', 'Phosphorus,mg': '1250',
                    'Potassium,mg': '4700', 'Sodium,mg': '2300', 'Zinc,mg': '11', 'Copper,mcg': '890', 'Manganese,mg': '2.2',
                    'Selenium,mcg': '55'}
            Vitamins = {'Vitamin A, mg RAE': '900', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600', 'Vitamin C, mg': '75',
                    'Thiamin, mg': '1.2', 'Riboflavin, mg': '1.3', 'Niacin, mg': '16', 'Vitamin B6, mg': '1.3',
                     'Vitamin B12, mcg': '2.4', 'Choline, mg': '550', 'Vitamin K, mcg': '75', 'Folate, mcg DFE': '400'}
        elif 18 < real_age <= 30:
            Macronutrients = {'Protein,g': '56', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130', 'Carbonhydrate,kcal': '55',
                              'DietaryFiber,g': '33.6', 'AddedSugars,kcal': '<10%', 'TotalFat,kcal': '22.5',
                              'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '17', 'LinolenicAcid,g': '1.6'}
            Minerals = {'Calcium,mg': '1000', 'Iron,mg': '8', 'Magnesium,mg': '400', 'Phosphorus,mg': '700', 'Potassium,mg': '4700',
                        'Sodium,mg': '2300', 'Zinc,mg': '11', 'Copper,mcg': '900', 'Manganese,mg': '2.3', 'Selenium,mcg': '55'}
            Vitamins = {'Vitamin A, mg RAE': '900', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600', 'Vitamin C, mg': '90',
                        'Thiamin, mg': '1.2', 'Riboflavin, mg': '1.3', 'Niacin, mg': '16', 'Vitamin B6, mg': '1.3',
                        'Vitamin B12, mcg': '2.4', 'Choline, mg': '550', 'Vitamin K, mcg': '120', 'Folate, mcg DFE': '400'}
        elif 30 < real_age <= 50:
             Macronutrients = {'Protein,g': '56', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130', 'Carbonhydrate,kcal': '55',
                               'DietaryFiber,g': '30.8', 'AddedSugars,kcal': '<10%', 'TotalFat,kcal': '22.5',
                               'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '17', 'LinolenicAcid,g': '1.6'}
             Minerals = {'Calcium,mg': '1000', 'Iron,mg': '8', 'Magnesium,mg': '420', 'Phosphorus,mg': '700', 'Potassium,mg': '4700',
                          'Sodium,mg': '2300', 'Zinc,mg': '11', 'Copper,mcg': '900', 'Manganese,mg': '2.3', 'Selenium,mcg': '55'}
             Vitamins = {'Vitamin A, mg RAE': '900', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600', 'Vitamin C, mg': '90',
                         'Thiamin, mg': '1.2', 'Riboflavin, mg': '1.3', 'Niacin, mg': '16', 'Vitamin B6, mg': '1.3',
                         'Vitamin B12, mcg': '2.4', 'Choline, mg': '550', 'Vitamin K, mcg': '120', 'Folate, mcg DFE': '400'}
        elif real_age > 50:
             Macronutrients = {'Protein,g': '56', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130', 'Carbonhydrate,kcal': '55',
                               'DietaryFiber,g': '28', 'AddedSugars,kcal': '<10%', 'TotalFat,kcal': '27',
                               'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '14', 'LinolenicAcid,g': '1.6'}
             Minerals = {'Calcium,mg': '1000', 'Iron,mg': '8', 'Magnesium,mg': '420', 'Phosphorus,mg': '700', 'Potassium,mg': '4700',
                         'Sodium,mg': '2300', 'Zinc,mg': '11', 'Copper,mcg': '900', 'Manganese,mg': '2.3', 'Selenium,mcg': '55'}
             Vitamins = {'Vitamin A, mg RAE': '900', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600', 'Vitamin C, mg': '90',
                         'Thiamin, mg': '1.2', 'Riboflavin, mg': '1.3', 'Niacin, mg': '16', 'Vitamin B6, mg': '1.7',
                         'Vitamin B12, mcg': '2.4', 'Choline, mg': '550', 'Vitamin K, mcg': '120', 'Folate, mcg DFE': '400'}
        else:
            raise ValueError
    if gender == u'女':
        if 3 < real_age <= 8:
             Macronutrients = {'Protein,g': '19', 'Protein,kcal': '20', 'Carbonhydrate,g': '130',
                               'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '16.8', 'AddedSugars,kcal': '<10%',
                               'TotalFat,kcal': '30', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '10',
                               'LinolenicAcid,g': '0.9'}
             Minerals = {'Calcium,mg': '1000', 'Iron,mg': '10', 'Magnesium,mg': '130', 'Phosphorus,mg': '500',
                         'Potassium,mg': '3800', 'Sodium,mg': '1900', 'Zinc,mg': '5', 'Copper,mcg': '440',
                         'Manganese,mg': '1.5', 'Selenium,mcg': '30'}
             Vitamins = {'Vitamin A, mg RAE': '400', 'Vitamin E,mg AT': '7', 'Vitamin D, IU': '600',
                         'Vitamin C, mg': '25', 'Thiamin, mg': '0.6', 'Riboflavin, mg': '0.6',
                         'Niacin, mg': '8', 'Vitamin B6, mg': '0.6', 'Vitamin B12, mcg': '1.2',
                         'Choline, mg': '250', 'Vitamin K, mcg': '55', 'Folate, mcg DFE': '200'}
        elif 8 < real_age <= 13:
             Macronutrients = {'Protein,g': '34', 'Protein,kcal': '20', 'Carbonhydrate,g': '130',
                               'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '22.4', 'AddedSugars,kcal': '<10%',
                               'TotalFat,kcal': '30', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '10',
                               'LinolenicAcid,g': '1'}
             Minerals = {'Calcium,mg': '1300', 'Iron,mg': '8', 'Magnesium,mg': '240', 'Phosphorus,mg': '1250',
                         'Potassium,mg': '4500', 'Sodium,mg': '2200', 'Zinc,mg': '8', 'Copper,mcg': '700',
                         'Manganese,mg': '1.6', 'Selenium,mcg': '40'}
             Vitamins = {'Vitamin A, mg RAE': '600', 'Vitamin E,mg AT': '11', 'Vitamin D, IU': '600',
            'Vitamin C, mg': '45', 'Thiamin, mg': '0.9', 'Riboflavin, mg': '0.9',
            'Niacin, mg': '12', 'Vitamin B6, mg': '1', 'Vitamin B12, mcg': '1.8',
            'Choline, mg': '375', 'Vitamin K, mcg': '60', 'Folate, mcg DFE': '300'}
        elif 13 < real_age <= 18:
             Macronutrients = {'Protein,g': '46', 'Protein,kcal': '20', 'Carbonhydrate,g': '130',
                               'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '25.2', 'AddedSugars,kcal': '<10%',
                               'TotalFat,kcal': '30', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '11',
                               'LinolenicAcid,g': '1.1'}
             Minerals = {'Calcium,mg': '1300', 'Iron,mg': '15', 'Magnesium,mg': '360', 'Phosphorus,mg': '1250',
                         'Potassium,mg': '4700', 'Sodium,mg': '2300', 'Zinc,mg': '9', 'Copper,mcg': '890',
                        'Manganese,mg': '1.6', 'Selenium,mcg': '55'}
             Vitamins = {'Vitamin A, mg RAE': '700', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600',
                         'Vitamin C, mg': '65', 'Thiamin, mg': '1', 'Riboflavin, mg': '1',
                         'Niacin, mg': '14', 'Vitamin B6, mg': '1.2', 'Vitamin B12, mcg': '2.4',
                         'Choline, mg': '400', 'Vitamin K, mcg': '75', 'Folate, mcg DFE': '400'}
        elif 18 < real_age <= 30:
            Macronutrients = {'Protein,g': '46', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130',
                              'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '28', 'AddedSugars,kcal': '<10%',
                              'TotalFat,kcal': '27.5', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '12',
                              'LinolenicAcid,g': '1.1'}
            Minerals = {'Calcium,mg': '1000', 'Iron,mg': '18', 'Magnesium,mg': '310', 'Phosphorus,mg': '700',
                        'Potassium,mg': '4700', 'Sodium,mg': '2300', 'Zinc,mg': '8', 'Copper,mcg': '900',
                        'Manganese,mg': '1.8', 'Selenium,mcg': '55'}
            Vitamins = {'Vitamin A, mg RAE': '700', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600',
                        'Vitamin C, mg': '75', 'Thiamin, mg': '1.1', 'Riboflavin, mg': '1.1',
                        'Niacin, mg': '14', 'Vitamin B6, mg': '1.3', 'Vitamin B12, mcg': '2.4',
                        'Choline, mg': '425', 'Vitamin K, mcg': '90', 'Folate, mcg DFE': '400'}
        elif 30 < real_age <= 50:
            Macronutrients = {'Protein,g': '46', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130',
                              'Carbonhydrate,kcal': '55', 'DietaryFiber,g': '25.2', 'AddedSugars,kcal': '<10%',
                              'TotalFat,kcal': '27.5', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '12',
                              'LinolenicAcid,g': '1.1'}
            Minerals = {'Calcium,mg': '1000', 'Iron,mg': '8', 'Magnesium,mg': '320', 'Phosphorus,mg': '700',
                        'Potassium,mg': '4700', 'Sodium,mg': '2300', 'Zinc,mg': '8', 'Copper,mcg': '900',
                        'Manganese,mg': '1.8', 'Selenium,mcg': '55'}
            Vitamins = {'Vitamin A, mg RAE': '700', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600',
                        'Vitamin C, mg': '75', 'Thiamin, mg': '1.1', 'Riboflavin, mg': '1.1',
                        'Niacin, mg': '14', 'Vitamin B6, mg': '1.3', 'Vitamin B12, mcg': '2.4',
                        'Choline, mg': '425', 'Vitamin K, mcg': '120', 'Folate, mcg DFE': '400'}
        elif real_age > 50:
            Macronutrients = {'Protein,g': '46', 'Protein,kcal': '22.5', 'Carbonhydrate,g': '130',
                              'Carbonhydrate,kcal': '45-65', 'DietaryFiber,g': '22.4', 'AddedSugars,kcal': '<10%',
                              'TotalFat,kcal': '27.5', 'SaturatedFat,kcal': '<10%', 'LinoleicAcid,g': '11',
                              'LinolenicAcid,g': '1.1'}
            Minerals = {'Calcium,mg': '1200', 'Iron,mg': '8', 'Magnesium,mg': '320', 'Phosphorus,mg': '700',
                        'Potassium,mg': '4700', 'Sodium,mg': '2300', 'Zinc,mg': '8', 'Copper,mcg': '900',
                        'Manganese,mg': '1.8', 'Selenium,mcg': '55'}
            Vitamins = {'Vitamin A, mg RAE': '700', 'Vitamin E,mg AT': '15', 'Vitamin D, IU': '600',
                        'Vitamin C, mg': '75', 'Thiamin, mg': '1.1', 'Riboflavin, mg': '1.1',
                        'Niacin, mg': '14', 'Vitamin B6, mg': '1.5', 'Vitamin B12, mcg': '2.4',
                        'Choline, mg': '425', 'Vitamin K, mcg': '90', 'Folate, mcg DFE': '400'}
        else:
            raise ValueError

    nutrition_list = [aaEER, Macronutrients['Protein,g'],
                      Macronutrients['Carbonhydrate,g'], Macronutrients['DietaryFiber,g'],
                      Macronutrients['TotalFat,kcal'], Minerals['Calcium,mg'],
                      Minerals['Iron,mg'], Minerals['Magnesium,mg'],
                      Minerals['Phosphorus,mg'], Minerals['Potassium,mg'], Minerals['Sodium,mg'], Minerals['Zinc,mg'],
                      Minerals['Manganese,mg'], Minerals['Selenium,mcg'], Vitamins['Vitamin A, mg RAE'], Vitamins['Vitamin E,mg AT'],
                      Vitamins['Vitamin C, mg'],  Vitamins['Riboflavin, mg'],
                      Vitamins['Niacin, mg'], Vitamins['Vitamin B6, mg'], Vitamins['Vitamin B12, mcg'], Vitamins['Choline, mg'],
                      Vitamins['Vitamin K, mcg'], Vitamins['Folate, mcg DFE']]
    for i in range(len(nutrition_list)):
        nutrition_list[i] = float(nutrition_list[i])
    print (nutrition_list)

    return nutrition_list

# https://wenku.baidu.com/view/7e9f286916fc700aba68fc14.html
# Estimated energy requirement in Chinese dietary(EER)


def EER_chinese(gender, age, activity_level):
    if age <= 1:
        err = 900 if gender == u'男' else 800
    if age == 2:
        pass


if __name__ == '__main__':
    age = raw_input("请输入您的年龄:")
    height = raw_input("请输入您的身高(cm):")
    weight = raw_input("请输入您的体重(kg):")
    gender = raw_input("请输入您的性别(男/女):").decode('utf8')
    activity_level = raw_input("请输入您的运动量(非常少/较少/较多/非常多):").decode('utf8')

    eer = EER(age, height, weight, gender, activity_level)
    print(eer)
    #nutrition(12, 65, 1.8, 'female', 'Active')
    nutrition(age, height, weight, gender, activity_level)
