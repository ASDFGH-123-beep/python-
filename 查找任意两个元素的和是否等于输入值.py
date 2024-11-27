"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1:
输入:nums=[2,7,11,15]，target=9输出:[0，1]
解释:因为nums[0l+nums[1l==9，返回[0，11
示例 2:
输入:nums=[3,2,4]，target = 6
输出:[1,2]
示例 3:
输入:nums=[3,3]，target=6输出:[0，1]
"""
nums=[]
while True:
    num=input("请输入数组，当输入空格停止录入：")
    if num ==' ':
        break
    try:
        number=int(num)
        nums.append(number)
    except ValueError:
        print("请输入一个有效的整数")
    print("数列：",nums)
count=len(nums)
target=int(input("请输入列表中任意两项相加的和："))
for i in range(count):
    i = +i
    for  j in range(i+1,):
        if nums[j]+nums[i]==target:
            print(f'[{i}, {j}]')
            break
        elif nums[i]+nums[j]!=target:
            print("未找到合适的数据")