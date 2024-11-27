"""
给你一个下标从0开始的整数数组 nums ，请你找到 最左边 的中间位置 middleIndex(也就是所有可能中间位置下标最小的一个)。
中间位置 middleIndex 是满足 nums [0]+ nums[1]+.. + nums [midleIndex-1] == nums [middleIndex+1]+ nums midleIndex+2]+..+nums[nums.length-1]的数组下标。
如果 middleIndex ==0，左边部分的和定义为0。类似的，如果 middleIndex==nums.length-1，右边部分的和定义为0。
请你返回满足上述条件 最左边 的 middleIndex ，如果不存在这样的中间位置，请你返回 -1。
示例 1:
输入:nums =[2,3,-1,8,4]输出:3解释:
下标 3之前的数字和为:2+3+-1=4下标 3 之后的数字和为:4=4
示例 2:
输入:nums =[1,-1,4]输出:2解释:下标 2 之前的数字和为:1 +-1 = 0下标 2 之后的数字和为:0
"""
"""回文数是指121或12321，左右的读取顺序一样[0,1,2,3,4,5]或[-5,-4,-3,-2,-1]"""
def MiddleIndex(nums):
    nums_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == nums_sum - left_sum - nums[i]:
            return i
        left_sum += nums[i]  #
    else:
        print("-1")
num1=[]
while True:
    num=input("请输入数组，当输入空格停止录入：")
    if num ==' ':
        break
    try:
        number=int(num)
        num1.append(number)
    except ValueError:
        print("请输入一个有效的整数")
    print("数列：",num1)
print(MiddleIndex(num1))