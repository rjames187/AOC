# calorie counting

f = open("calorie.txt")

max_cals = 0
cur_cals = 0

while True:
    line = f.readline()
    if not line:
        max_cals = max(cur_cals, max_cals)
        break
    
    if line.strip() == "":
        max_cals = max(cur_cals, max_cals)
        cur_cals = 0
        continue
    
    cur_cals += int(line)
    
    

f.close()

print(f"The most calories being carried by one elf is {max_cals}.")