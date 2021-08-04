# 猜数字
#     需求:系统随机产生一个数字(0~10000),让用户从键盘输入
#         1.如果猜中,恭喜
#         2.如果猜的比系统的数字大,提示:大了
#         3.小了同理
# 金币功能:
#     需求:
#         1.先登录
#         2.玩家初始化5000硬币,猜错扣除500.金币不够,系统锁定
#         3.猜中,奖励10000硬币,选择是否进行第二轮

import random

class Day3:

    def __init__(self):
        self.num = random.randint(0,10000)
        print(self.num)
        self.coin = 5000

    def guess(self):
        while self.coin > 0:
            try:
                x = int(input("请输入您猜的数字(0~10000)\n"))
            except Exception as e:
                print("请输入0~10000的整数")
                continue

            if x > self.num:
                self.coin -= 500
                print("很可惜,猜错了,您猜的数字比答案大,金币-500,还剩%d"%self.coin)
            elif x == self.num:
                self.coin += 10000
                print("恭喜您,猜对了,金币+10000,现在您有金币%d"%self.coin)
                if input("是否继续游戏(y/n)") == 'y':
                    continue
                else:
                    print("游戏结束,您的金币为%d"%self.coin)
                    break
            elif x < self.num:
                self.coin -= 500
                print("很可惜,猜错了,您猜的数字比答案小,金币-500,还剩%d"%self.coin)


            if self.coin == 0:
                print("金币用尽,游戏结束")

if __name__ == '__main__':
    test = Day3()
    test.guess()







