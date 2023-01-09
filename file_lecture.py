

from pathlib import Path

nums = []
# opens 
with open(Path(r"C:\Users\wgatl\OneDrive\Desktop\CPSC230\numbers.txt"), 'r') as file:
    for line in file:
        num = int(line)
        nums.append(num)

print(min(nums))


