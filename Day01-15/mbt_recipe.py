#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


# 随机选取食材
def get_ingredients(n):
    ingredients = ['鸡肉', '牛肉', '猪肉', '鱼', '蔬菜', '豆腐', '鸡蛋', '土豆', '洋葱', '青椒', '红椒', '胡萝卜', '蘑菇', '木耳', '虾仁', '蟹肉', '虾仁']
    return random.sample(ingredients, n)


# 随机选取调料
def get_seasoning():
    seasoning = ['盐', '酱油', '味精', '辣椒', '姜', '蒜']
    return random.sample(seasoning, random.randint(1, len(seasoning)))


# 随机选取烹饪方法
def get_recipe():
    cooking_methods = {
        '爆炒': '将食材放入热锅中，在高温下快速翻炒，出锅装盘',
        '煮煎': '将食材放入沸水中煮熟，然后放入平底锅中煎熟',
        '油炸': '将食材裹上面糊，放入热油中炸至金黄色',
        '煎烤': '将食材放入平底锅中煎熟，然后放入烤箱中用高温烘烤',
        '蒸煮': '将食材放入蒸锅中蒸熟，然后放入锅中加水或汤料煮至入味',
        '焖炖': '将食材放入锅中加水或汤料焖煮煮至熟透',
        '红烧': '将食材放入锅中煮熟，然后烧煮辅料至入味',
        '烤炸': '将食材放入烤箱中用高温烘烤，然后放入热油中炸至金黄色',
    }
    cooking_method = random.choice(list(cooking_methods))
    lst = list(cooking_methods)
    print(lst)
    method_step = cooking_methods[cooking_method]

    ingredients = get_ingredients(3)
    method_step = method_step.replace('食材', '、'.join(ingredients))

    seasoning = '、'.join(get_seasoning())

    # 生成菜谱名称
    dish_name = cooking_method + ingredients[0]
    # 生成菜谱步骤
    method_step = method_step.format(ingredients[0], ingredients[1], ingredients[2], seasoning)
    # 生成菜谱
    recipe = f'{dish_name}：{method_step},加入{seasoning}调味，出锅装盘。'
    return recipe


recipe = get_recipe()
print(recipe)
