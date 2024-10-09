name = input('请输入你的名字：')
print('欢迎', name, '现在开始知识问答。')

score = 0

answer1 = input('问题1：地球上最大的洋是什么洋？')
if answer1 == '太平洋':
    print('回答正确！')
    score = score + 1
else:
    print('回答错误！')

answer2 = input('问题2：10-5*2=？（填写数字）')
if int(answer2) == 0:
    print('回答正确！')
    score = score + 1
else:
    print('回答错误！')

answer3 = input('问题3：1英里等于多少千米？')
if float(answer3) == 1.6:
    print('回答正确！')
    score = score + 1
else:
    print('回答错误！')

if score == 0:  # 不同分数，提示不同
    print(name, '得分为0，需要加油！')
if score == 1:
    print(name, '得分为1，继续努力！')
if score == 2:
    print(name, '得分为2，做得不错！')
if score == 3:
    print(name, '得分为3，非常棒！')
