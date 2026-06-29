data =[(11,40),(2,4),(6,9)]
result =sorted(data ,key=lambda x: x[1])
result2 =sorted(data ,key=lambda x: x[0]) #sorted by using the first place of every entry
print(result)


nums =[4,7,2,9,8,1,3,0 ]
result3 =list(map(lambda x :x**2,nums))
print(result3)

result4 =list(filter(lambda x: x%2==0 ,nums))
print(result4)


from functools import reduce
marks =[60,65,79,80,78]
result5 =reduce(lambda x,y: x+y,marks)
print(result5)
