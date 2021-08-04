


# 实现输入10个数字，并打印10个数的求和结果
def input10():
    listInput = []
    print("请输入10个数字")
    for i in range(10):
        try:
            listInput.append(int(input()))
        except ValueError as e:
            print("请输入数字!")
            listInput.clear()
            input10()
            break
    if listInput:
        print("和为"+(str(sum(listInput))))

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
def input10_2():
    listInput = []
    print("请输入10个数字")
    for i in range(10):
        try:
            listInput.append(int(input()))
        except ValueError as e:
            print("请输入数字!")
            listInput.clear()
            input10_2()
            break
    if listInput:
        print("最大值为" + (str(max(listInput))))
        print("和为" + (str(sum(listInput))))
        print("平均数为" + (str(sum(listInput) / len(listInput))))

# 从键盘输入任意三边，判断是否能形成三角形，
# 若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
def triangularJudge():

    # 判断三角形形状,a<b<c
    def judge(a,b,c):
        if (a+b) < c:
            return "不能构成三角形"
        elif (a**2 + b**2) == c**2:
            return "直角三角形"
        elif a == b and b == c:
            return "等边三角形"
        elif a == b:
            return "等腰三角形"
        else:
            return "普通三角形"


    listInput = []
    print("请输入3个数字")
    for i in range(3):
        try:
            listInput.append(int(input()))
        except ValueError as e:
            print("请输入数字!")
            listInput.clear()
            triangularJudge()
            break
    if listInput:
        listInput.sort()
        # 判断
        print(judge(*listInput))

# 有以下两个数，使用+，-号实现两个数的调换。
A = 56
B = 78

A = A + B
B = A - B
A = A - B

print(A,B)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
def login():
    for i in range(3):
        print("请输入用户名,密码")
        usr = input()
        pwd = input()
        if usr == 'root' and pwd == 'admin':
            print('登录成功')
            return True
        print("用户名或密码有误")
    print("登录失败")
    return False        # 锁定功能靠返回值实现

# 使用while编程实现求1~100以内的数的和！
def sum():
    sum = 0
    x = 1
    while x < 101:
        sum = sum + x
        x +=1
    return sum
print(sum())

# 一只青蛙掉在井里了，井高20米，
# 青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出
def frog():
    height = 20
    frog = 0
    day = 0
    while True:
        day += 1
        frog += 3
        if frog >= height:
            break
        frog -= 2
    print('第%d天爬出来'%day)

# 从键盘输入6课成绩，并统计6课成绩总分数、平均分、最高分、最低分
def grades():
    listInput = []
    print("请输入6门课程的成绩")
    for i in range(6):
        try:
            listInput.append(int(input()))
        except ValueError as e:
            print("请输入数字!")
            listInput.clear()
            grades()
            break
    if listInput:
        print("总分为" + (str(sum(listInput))))
        print("平均分为" + (str(sum(listInput) / len(listInput))))
        print("最高分为" + (str(max(listInput))))
        print("最低分为" + (str(min(listInput))))


if __name__ == '__main__':

    # input10()
    # input10_2()
    # triangularJudge()
    # a,b = swap(a,b)
    # login()
    # sum100()
    # frog()
    # grades()

    pass


# 编程实现下列图形的打印
# * 组成的三角形
# 这里设画布长度是21
def draw(n):
    def getLine(long=21):
        list = []
        for i in range(long):
            list.append(' ')
        return list

    for i in range(n+1):
        line = getLine()
        # 奇数
        if i%2:
            for x in range(i):
                # 奇数的偶数项为*
                if not x%2:
                    line[10+x] = '*'
                    line[10-x] = '*'
        # 偶数
        else:
             for x in range(i):
                 # 偶数的奇数项为*
                 if x%2:
                     line[10 + x] = '*'
                     line[10 - x] = '*'
                 pass
        # 直接打印有逗号,不好看print(line)
        for data in line:
            print(data,end='')
        print('')

# 使用while循环实现99乘法表的打印
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    j = 1
    while j <= i :
        print(f'{i}*{j}={i*j}',end='\t')
        j += 1
    print()

# 编程实现99乘法表的倒叙打印
def reverseMultiplication():
    list = [x for x in range(1,10)]
    list.reverse()
    for i in list:
        for x in range(1, i + 1):
            print('%d*%d=%d' % (x, i, x * i), end=' ')
        print('')







