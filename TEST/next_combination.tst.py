next = next_combination([],['a', 'b', 'c', 'd', 'e'])
while(next!=None):
    print(next,get_combination_binlist(next,['a', 'b', 'c', 'd', 'e']))
    next = next_combination(next,['a', 'b', 'c', 'd', 'e'])

['a'] [0, 0, 0, 0, 1]
['b'] [0, 0, 0, 1, 0]
['c'] [0, 0, 1, 0, 0]
['d'] [0, 1, 0, 0, 0]
['e'] [1, 0, 0, 0, 0]
['a', 'b'] [0, 0, 0, 1, 1]
['a', 'c'] [0, 0, 1, 0, 1]
['b', 'c'] [0, 0, 1, 1, 0]
['a', 'd'] [0, 1, 0, 0, 1]
['b', 'd'] [0, 1, 0, 1, 0]
['c', 'd'] [0, 1, 1, 0, 0]
['a', 'e'] [1, 0, 0, 0, 1]
['b', 'e'] [1, 0, 0, 1, 0]
['c', 'e'] [1, 0, 1, 0, 0]
['d', 'e'] [1, 1, 0, 0, 0]
['a', 'b', 'c'] [0, 0, 1, 1, 1]
['a', 'b', 'd'] [0, 1, 0, 1, 1]
['a', 'c', 'd'] [0, 1, 1, 0, 1]
['b', 'c', 'd'] [0, 1, 1, 1, 0]
['a', 'b', 'e'] [1, 0, 0, 1, 1]
['a', 'c', 'e'] [1, 0, 1, 0, 1]
['b', 'c', 'e'] [1, 0, 1, 1, 0]
['a', 'd', 'e'] [1, 1, 0, 0, 1]
['b', 'd', 'e'] [1, 1, 0, 1, 0]
['c', 'd', 'e'] [1, 1, 1, 0, 0]
['a', 'b', 'c', 'd'] [0, 1, 1, 1, 1]
['a', 'b', 'c', 'e'] [1, 0, 1, 1, 1]
['a', 'b', 'd', 'e'] [1, 1, 0, 1, 1]
['a', 'c', 'd', 'e'] [1, 1, 1, 0, 1]
['b', 'c', 'd', 'e'] [1, 1, 1, 1, 0]
['a', 'b', 'c', 'd', 'e'] [1, 1, 1, 1, 1]



[]    [0, 0, 0, 0, 0]                 0
##########################################
#
['a'] [0, 0, 0, 0, 1]                 1
['b'] [0, 0, 0, 1, 0]                 2
['c'] [0, 0, 1, 0, 0]                 3
['d'] [0, 1, 0, 0, 0]                 4
['e'] [1, 0, 0, 0, 0]                 5
################################################
#元素个数是2 则
# 0,0,0,1 开头  1*1 的对角线是 1 的矩阵
#
['a', 'b'] [0, 0, 0, 1, |1|]            6
#
['a', 'c'] [0, 0, 1, |0, 1|]            7
['b', 'c'] [0, 0, 1, |1, 0|]            8
#
['a', 'd'] [0, 1, |0, 0, 1|]            9
['b', 'd'] [0, 1, |0, 1, 0|]            10
['c', 'd'] [0, 1, |1, 0, 0|]            11
#
['a', 'e'] [1, |0, 0, 0, 1|]            12
['b', 'e'] [1, |0, 0, 1, 0|]            13
['c', 'e'] [1, |0, 1, 0, 0|]            14
['d', 'e'] [1, |1, 0, 0, 0|]            15
##################################################################
#元素个数是3 则
# 0 开头  (3+1)*(3+1) 的对角线是 0 的矩阵
['a', 'b', 'c'] [0, |0, 1, 1, 1|]------>16
['a', 'b', 'd'] [0, |1, 0, 1, 1|]------>17
['a', 'c', 'd'] [0, |1, 1, 0, 1|]------>18
['b', 'c', 'd'] [0, |1, 1, 1, 0|]
# 1 0 开头 (2+1)*(2+1) 的对角线是 0 的矩阵
['a', 'b', 'e'] [1, 0, |0, 1, 1|]
['a', 'c', 'e'] [1, 0, |1, 0, 1|]
['b', 'c', 'e'] [1, 0, |1, 1, 0|]
# 1 1 0 开头 (1+1)*(1+1) 的对角线是 0 的矩阵
['a', 'd', 'e'] [1, 1, 0, |0, 1|]
['b', 'd', 'e'] [1, 1, 0, |1, 0|]
# 1 1 1 0 开头 (0+1)*(0+1) 的对角线是 0 的矩阵
['c', 'd', 'e'] [1, 1, 1, 0, |0|]
###############################################
# 元素个数是 4 则
# (4+1) * (4+1) 的对角线是 0 的矩阵
['a', 'b', 'c', 'd'] [0, 1, 1, 1, 1]
['a', 'b', 'c', 'e'] [1, 0, 1, 1, 1]
['a', 'b', 'd', 'e'] [1, 1, 0, 1, 1]
['a', 'c', 'd', 'e'] [1, 1, 1, 0, 1]
['b', 'c', 'd', 'e'] [1, 1, 1, 1, 0]
#################################################
#元素个数是5 全 1
['a', 'b', 'c', 'd', 'e'] [1, 1, 1, 1, 1]




next = next_combination([],['a', 'b', 'c', 'd','e','f'])
while(next!=None):
    print(next,get_combination_binlist(next,['a', 'b', 'c', 'd','e','f']))
    next = next_combination(next,['a', 'b', 'c', 'd','e','f'])


[]

['a'] [0, 0, 0, 0, 0, 1]
['b'] [0, 0, 0, 0, 1, 0]
['c'] [0, 0, 0, 1, 0, 0]
['d'] [0, 0, 1, 0, 0, 0]
['e'] [0, 1, 0, 0, 0, 0]
['f'] [1, 0, 0, 0, 0, 0]
#2  1  ->  6-1
#2  1  ->  5
['a', 'b'] [0, 0, 0, 0, 1, |1|]
['a', 'c'] [0, 0, 0, 1, |0, 1|]
['b', 'c'] [0, 0, 0, 1, |1, 0|]
['a', 'd'] [0, 0, 1, |0, 0, 1|]
['b', 'd'] [0, 0, 1, |0, 1, 0|]
['c', 'd'] [0, 0, 1, |1, 0, 0|]
['a', 'e'] [0, 1, |0, 0, 0, 1|]
['b', 'e'] [0, 1, |0, 0, 1, 0|]
['c', 'e'] [0, 1, |0, 1, 0, 0|]
['d', 'e'] [0, 1, |1, 0, 0, 0|]
['a', 'f'] [1, |0, 0, 0, 0, 1|]
['b', 'f'] [1, |0, 0, 0, 1, 0|]
['c', 'f'] [1, |0, 0, 1, 0, 0|]
['d', 'f'] [1, |0, 1, 0, 0, 0|]
['e', 'f'] [1, |1, 0, 0, 0, 0|]

#3   2 -> 6-2      
['a', 'b', 'c'] [0, 0,|0, 1, 1, 1|]
['a', 'b', 'd'] [0, 0,|1, 0, 1, 1|]
['a', 'c', 'd'] [0, 0,|1, 1, 0, 1|]
['b', 'c', 'd'] [0, 0,|1, 1, 1, 0|]

['a', 'b', 'e'] [0, 1, 0,|0, 1, 1|]
['a', 'c', 'e'] [0, 1, 0,|1, 0, 1|]
['b', 'c', 'e'] [0, 1, 0,|1, 1, 0|]

['a', 'd', 'e'] [0, 1, 1,|0, 0, 1|]
['b', 'd', 'e'] [0, 1, 1,|0, 1, 0|]
['c', 'd', 'e'] [0, 1, 1,|1, 0, 0|]

['a', 'b', 'f'] [1, 0, 0,|0, 1, 1|]
['a', 'c', 'f'] [1, 0, 0,|1, 0, 1|]
['b', 'c', 'f'] [1, 0, 0,|1, 1, 0|]

['a', 'd', 'f'] [1, 0, 1,|0, 0, 1|]
['b', 'd', 'f'] [1, 0, 1,|0, 1, 0|]
['c', 'd', 'f'] [1, 0, 1,|1, 0, 0|]

['a', 'e', 'f'] [1, 1, |0, 0, 0, 1|]
['b', 'e', 'f'] [1, 1, |0, 0, 1, 0|]
['c', 'e', 'f'] [1, 1, |0, 1, 0, 0|]
['d', 'e', 'f'] [1, 1, |1, 0, 0, 0|]

['a', 'b', 'c', 'd'] [0, |0, 1, 1, 1, 1|]
['a', 'b', 'c', 'e'] [0, |1, 0, 1, 1, 1|]
['a', 'b', 'd', 'e'] [0, |1, 1, 0, 1, 1|]
['a', 'c', 'd', 'e'] [0, |1, 1, 1, 0, 1|]
['b', 'c', 'd', 'e'] [0, |1, 1, 1, 1, 0|]

['a', 'b', 'c', 'f'] [1, 0,| 0, 1, 1, 1|]
['a', 'b', 'd', 'f'] [1, 0,| 1, 0, 1, 1|]
['a', 'c', 'd', 'f'] [1, 0,| 1, 1, 0, 1|]
['b', 'c', 'd', 'f'] [1, 0,| 1, 1, 1, 0|]

['a', 'b', 'e', 'f'] [1, 1, 0, |0, 1, 1|]
['a', 'c', 'e', 'f'] [1, 1, 0, |1, 0, 1|]
['b', 'c', 'e', 'f'] [1, 1, 0, |1, 1, 0|]
['a', 'd', 'e', 'f'] [1, 1, 1, 0, |0, 1|]
['b', 'd', 'e', 'f'] [1, 1, 1, 0, |1, 0|]
['c', 'd', 'e', 'f'] [1, 1, 1, 1, 0, |0|]

['a', 'b', 'c', 'd', 'e'] [0, 1, 1, 1, 1, 1]
['a', 'b', 'c', 'd', 'f'] [1, 0, 1, 1, 1, 1]
['a', 'b', 'c', 'e', 'f'] [1, 1, 0, 1, 1, 1]
['a', 'b', 'd', 'e', 'f'] [1, 1, 1, 0, 1, 1]
['a', 'c', 'd', 'e', 'f'] [1, 1, 1, 1, 0, 1]
['b', 'c', 'd', 'e', 'f'] [1, 1, 1, 1, 1, 0]
['a', 'b', 'c', 'd', 'e', 'f'] [1, 1, 1, 1, 1, 1]

