num = [2, 3, -10, 4, -3, 5, 10]
num2 = [0]

def solve(n):
    min, max = 0, 0
    for i in range(1, len(n)):
        if n[i] > max:
            max = n[i]
        if n[i] < min:
            min = n[i]
    return min + max
	
print(solve(num2))
