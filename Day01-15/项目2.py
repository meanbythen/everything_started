car = []
state = '运行中'
while state == '运行中':
    print('-' * 20)
    print('1. 添加商品')
    print('2. 展示购物车')
    print('3. 移除商品')
    print('4. 结算')
    print('q. 退出')
    choice = input('请选择操作：')

    if choice.strip() == '1':
        product = input('添加商品名称：')
        car.append(product)
        print('已添加', product)

    elif choice.strip() == '2':
        if len(car) == 0:
            print('购物车中没有商品')
        else:
            print('购物车中的商品：')
            for i in car:
                print(i)

    elif choice.strip() == '3':
        deleted = input('移除商品名称：')
        if deleted in car:
            car.remove(deleted)
            print('已移除', deleted)
        else:
            print('购物车中没有', deleted)

    elif choice.strip() == '4':
        total_cost = 0.0
        settled = []
        for i in car:
            if i == '苹果':
                total_cost += 5
                settled.append(i)
            elif i == '橘子':
                total_cost += 8
                settled.append(i)
            elif i == '香蕉':
                print(i, '缺货无法结算')
            else:
                print(i,'未识别，无法结算')
        if total_cost >= 10.0:
            total_cost *= 0.9
        for i in settled:
            car.remove(i)
        print(f'总共 {total_cost:.2f} 元')

    elif choice.strip() == 'q':
        state = '结束'
