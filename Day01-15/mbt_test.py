time = 0


def calculate_average(numbers):
    """
    计算列表中数字的平均值
    :param numbers: 输入的列表
    :return: 返回列表中数字的平均值
    """
    try:
        total = sum(numbers)  # 计算列表中数字的总和,sum()函数只能用于可迭代对象
        count = len(numbers)  # 计算列表中数字的个数
        average = total / count  # 计算列表中数字的平均值
    except AttributeError:  # 如果输入的不是一个可迭代对象，会抛出AttributeError异常
        print("Error: Input is not a iterable object")
    except ZeroDivisionError:  # 如果输入的列表为空，会抛出ZeroDivisionError异常，但返回平均数0
        print('Input is a empty list')
        return 0
    except TypeError:  # 如果输入的列表中包含非数字值，会抛出TypeError异常，返回列表本身
        print("Error: Input contains non-numeric values")
        return numbers
    else:  # 如果没有异常，则返回计算的平均值
        print(f"{numbers} Average Execute Success")
        return average
    finally:  # 无论是否发生异常，都会执行finally语句块，全局变量time加1计算测试次数，并打印测试结果
        global time
        time += 1
        print(f"The {time}th test result is:")


num1 = [1, 2, 3, 4, 5]
num2 = (1, 2, 3, 4, 5)
num3 = {1, 2, 3, 4, 5}
num4 = [1, 2, 'a', 4, 5]
num5 = []
num6 = 1
num7 = 3.14
num8 = [3.14, 1.73, 2.71, 1.41, 1.62]

testData = [num1, num2, num3, num4, num5, num6, num7, num8]
for index, numbers in enumerate(testData):
    average = calculate_average(numbers)
    print(f"{index + 1}:{numbers} average is:{average}")
