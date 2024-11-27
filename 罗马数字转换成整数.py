"""
罗马数字包含以下七种字符:I，，，，(),D 和 M。
数值-ng易1005001000
字符
H>XU
例如，罗马数字 2 写做 II，即为两个并列的1。(12写做XII)，即为+II)。(27写做XXVII,即为JXX+V+II。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如4不写做IIII，而是IV。数字1在数字5 的左边，所表示的数等于大数5
 减小数1得到的数值 4同样地，数字9表示为IX。这个特殊的规则只适用于以下六种情况:
I可以放在 v(5)和 x(10) 的左边，来表示 4和
X可以放在L(50) 和 c(100) 的左边，来表示 40和 90。
c可以放在 D(500)和 M(1000) 的左边，来表示 400 和 900。
给正岁马数子，将具转换成整数。
示例 1:
输入:S="III"输出:3
示例 2:
输入:S =“IV"输出:4
示例 3:
输入:s =“IX"输出:9
示例 4:
输入:S ="LVIII'输出:解释:L=50，V=5，III =3.
示例 5:
输入:S="MCMXCIV'输出:1994解释:M=1000，CM=900，XC=90，IV=4
"""
def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    result = 0
    for char in reversed(s.upper()):#反转序列的元素
        value = roman_dict[char]#数值对应
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
roman_num = input("请输入你要转换的罗马数字：")
print("对应的整数是：", roman_to_int(roman_num))
