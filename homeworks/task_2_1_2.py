def summation():
    numbers = input()
    nums = numbers.split()
    элементОдин = []
    элементДва = []
    summAnswer = 0
    for i in range(len(nums)):
        if int(nums[i]) < 0:
            элементОдин.append(2 * abs(int(nums[i])))
        else:
            элементОдин.append(int(nums[i]))
    элементОдин.sort()
    print(элементОдин)
    for j in range(len(элементОдин)):
        элементДва.append(элементОдин[j]/элементОдин[len(элементОдин)-1])
    print(элементДва)
    for b in range(len(элементДва)):
        summAnswer += round(элементДва[b],1)
    print(summAnswer)


summation()

print(summation())
