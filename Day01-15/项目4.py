import random

# 随机选取食材


def get_ingredients(n):
    ingredients = ['土豆', '洋葱', '胡萝卜', '青椒', '番茄', '鸡肉', '牛肉', '羊肉', '鱼肉']
    return random.sample(ingredients, n)

# 随机选取调料


def get_seasoning():
    seasonings = ['盐', '酱油', '味精', '辣椒', '姜', '蒜']
    return random.sample(seasonings, random.randint(1, 3))

# 生成食谱


def make_recipe():
    # 定义不同烹饪方法的步骤
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
    
    # 随机选取烹饪方法
    cooking_method = random.choice(list(cooking_methods))
    method_steps = cooking_methods[cooking_method]

    # 随机选取食材
    ingredients = get_ingredients(3)
    method_steps = method_steps.replace('食材', '、'.join(ingredients))

    # 随机选取调料
    seasoning = '、'.join(get_seasoning())

    # 生成食谱名称
    dish_name = cooking_method + ingredients[0]
    
    # 将随机生成的食材、烹饪方法和调料填入模板
    recipe = f'{dish_name}：{method_steps}，加入{seasoning}调味即可。'
    return recipe


recipe = make_recipe()
print(recipe)
