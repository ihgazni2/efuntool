prev = prev_combination(['a', 'b', 'c', 'd', 'e'],['a', 'b', 'c', 'd', 'e'])
while(prev!=None):
    print(prev,get_combination_binlist(prev,['a', 'b', 'c', 'd', 'e']))
    prev = prev_combination(prev,['a', 'b', 'c', 'd', 'e'])


['b', 'c', 'd', 'e'] [1, 1, 1, 1, 0]
['a', 'c', 'd', 'e'] [1, 1, 1, 0, 1]
['a', 'b', 'd', 'e'] [1, 1, 0, 1, 1]
['a', 'b', 'c', 'e'] [1, 0, 1, 1, 1]
['a', 'b', 'c', 'd'] [0, 1, 1, 1, 1]
['c', 'd', 'e'] [1, 1, 1, 0, 0]
['b', 'd', 'e'] [1, 1, 0, 1, 0]
['a', 'd', 'e'] [1, 1, 0, 0, 1]
['b', 'c', 'e'] [1, 0, 1, 1, 0]
['a', 'c', 'e'] [1, 0, 1, 0, 1]
['a', 'b', 'e'] [1, 0, 0, 1, 1]
['b', 'c', 'd'] [0, 1, 1, 1, 0]
['a', 'c', 'd'] [0, 1, 1, 0, 1]
['a', 'b', 'd'] [0, 1, 0, 1, 1]
['a', 'b', 'c'] [0, 0, 1, 1, 1]
['d', 'e'] [1, 1, 0, 0, 0]
['c', 'e'] [1, 0, 1, 0, 0]
['b', 'e'] [1, 0, 0, 1, 0]
['a', 'e'] [1, 0, 0, 0, 1]
['c', 'd'] [0, 1, 1, 0, 0]
['b', 'd'] [0, 1, 0, 1, 0]
['a', 'd'] [0, 1, 0, 0, 1]
['b', 'c'] [0, 0, 1, 1, 0]
['a', 'c'] [0, 0, 1, 0, 1]
['a', 'b'] [0, 0, 0, 1, 1]
['e'] [1, 0, 0, 0, 0]
['d'] [0, 1, 0, 0, 0]
['c'] [0, 0, 1, 0, 0]
['b'] [0, 0, 0, 1, 0]
['a'] [0, 0, 0, 0, 1]
[] [0, 0, 0, 0, 0]

