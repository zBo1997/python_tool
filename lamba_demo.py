print((lambda x,y:x+y)(1 , 2))
print((lambda x:x*x)(1))
print((lambda x,y:x//y)(1 , 2)) ## integer division
print((lambda x,y:x/y)(1 , 2)) ## float division
print((lambda x,y:x*y)(1 , 2))
result = lambda x,y:x+y
lambda_result = result(2,5)
print(lambda_result)