def genNums():
    import random
    nums = ['0','1','2','3','4','5','6','7','8','9']
    return [random.choice(nums) for _ in range(4)]

