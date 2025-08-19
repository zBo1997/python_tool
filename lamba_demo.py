print((lambda x,y:x+y)(1 , 2))
print((lambda x:x*x)(1))
print((lambda x,y:x//y)(1 , 2)) ## integer division
print((lambda x,y:x/y)(1 , 2)) ## float division
print((lambda x,y:x*y)(1 , 2))
result = lambda x,y:x+y
lambda_result = result(2,5)
print(lambda_result)


## filter
result_filter_nums = filter (lambda x: x%2 ==0, [1,2,3,4,5,6,7,8,9,10]) ## filter even numbers
print(list(result_filter_nums))

## sorted
students = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 28}]
result_sorted = sorted(students,key=lambda x : x['age'], reverse=True) ## sort by age in descending order
print(result_sorted)

## map
students_map = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 28}]
result_map = map(lambda x:x['name'],students_map)
print(list(result_map))
