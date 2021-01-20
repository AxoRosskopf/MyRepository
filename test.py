x=0
nums = [1,3,4,3]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

if __name__ == "__main__":
    if x == 4:
        while x >= 20:
            print ("not")
    print("****New exercise = Found the SMALLER number in a list*****")
    lst=[3,4,6,1,3,6,8,3,1,-2]
    z=max(lst)
    for y in lst:
        if z>y:
            z=y
            print("Min",z)
        elif y==max(lst):
            print("Max", y)
        else:
            print("  ",y)


#ddddd
    print("BIGGER NUMBER:", max(lst), " SMALLER NUMBER:",z)

    pass
