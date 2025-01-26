import uuid

# Generate a UUID
role_assignment_id = str(uuid.uuid4())

# Print or use role_assignment_id in your code
print("Generated Role Assignment ID:", role_assignment_id)


list1  = [1,9,5,3,5,7,5,6,10]
print(list1)
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]>list1[j]):
            temp = list1[j]
            list1[j] = list1[i]
            list1[i] = temp
print(list1)
print(list1[-1])
print(sum(list1))

n = 10
a = 0
b = 1
sum = a+b
l1 = []
l1.append(a)
l1.append(b)
print(l1)
for i in range(1,n-1):
    l1.append(sum)
    a=b
    b=sum
    sum = a+b
print(l1)