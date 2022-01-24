num = {
    1: 1,
    2: 4,
    3: 7,
    4: 199,
    5: 750
}

def sum(nums):
    s = 0
    for n in nums.values():
        s += n
    return s

def replace(nums):
    print(nums.values())
    key = int(input("Input the key to change:   "))
    val = int(input("Input the value you want to change it to:  "))
    nums.update({key: val})

def pop(nums):
    print(nums.values())
    key = int(input("Input the key to change:   "))
    nums.pop(key)

s = sum(num)
print(s)

pop(num)
print(num.values())
print(type(num))
print(len(num))
print(num.items())