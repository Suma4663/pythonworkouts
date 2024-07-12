
def sumof(numbers):
    return sum(numbers)

print(sumof([1,2,3,4,5]))

def evensumof(sumof,numbers):
    sum_of_args=sumof(numbers)
    return sum_of_args*sum_of_args

print(evensumof(sumof,[1,2,3,4,5]))

#Lambda function to filter a list
lst=[10000,20000,5000,25000,9000,15000]
lambda_filter=lambda x:x>10000
list2 = list(filter(lambda_filter,lst))
print (list2)

def outerfunction(text):
    def innerfunction():
        print(text)
    innerfunction()

if __name__ == '__main__':
    outerfunction("Hello gurl!!!")

lst=[1,'d']

print(lst)

capitals = {'India':'New Delhi', 'USA':'New York', 'Pakistan':'Islamabad'}

print(capitals['India'])
print(capitals)
capitals.update({'Malaysia':'Kuala Lumpur'})
print(capitals)
print(capitals.get('Australia','Not in dict'))


print(len("Inceptez Technologies"))
print(len(["Inceptez","Technologies"]))
print(len({"Name":"Inceptez","Type":"Technologies"}))

