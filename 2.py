def fibonacci(n):
    nums = [1, 1]

    for i in range(2, n):
        num = nums[i-1] + nums[i-2]
        nums.append(num)

    print(nums)

n = int(input('Enter the number of numbers: '))
fibonacci(n)
