nums = [-1,1,2,3,1]
target = 2

def countTargetPairs(nums, target):
    antwoord = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):  
            if nums[i] + nums[j] < target:
                antwoord += 1
    
    print(antwoord)
countTargetPairs(nums, target)
