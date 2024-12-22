"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] 
is the number of days you have to wait after the ith day to get a warmer temperature. 

If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""

temperatures = [55,38,53,81,61,93,97,32,43,78]

def dailyTemperaturesBruteforce(temperatures):
    #Using bruteforce should work at 0(n²), but I believe this is a stack operator exercice
        stack = [0] * len(temperatures)
        indices = 0
        indexfixe = 0 #Index that gets iterated on, moves by 1 at each iteration of the for loop
        
        try: #Bruteforce method that gets time limit exceeded
            for x in temperatures:
                indices = indexfixe #Resets the indices iterated on at the same value of  the index that gets iterated on in the for loop
                while x >= temperatures[indices+1]:
                    indices +=1
                    if indices+1 >= len(temperatures): #If the temperature iterated on is the last one to be this high in the array, set it to 0 (there will not be a higher temperature succeeding)
                        stack[indexfixe] = 0 #set it to 0                        
                        indices = indexfixe #reset the loop
                        break
                    
                if x < temperatures[indices+1]:
                    stack[indexfixe] = (indices+1) - indexfixe
                else:
                    indexfixe +=1
                    continue
                
                indexfixe += 1
                
        except IndexError:
            pass
        print(stack)
dailyTemperaturesBruteforce(temperatures)

"""
Cleaner format:

def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = []

    for i in range(n):
        count = 1
        j = i + 1
        while j < n:
            if temperatures[j] > temperatures[i]:
                break
            j += 1
            count += 1
        count = 0 if j == n else count
        res.append(count)
    return res
"""

#Actual solution using stack:
def dailyTemperatures(temperatures):
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

#print(dailyTemperatures(temperatures))