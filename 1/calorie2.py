# calorie counting

f = open("calorie.txt")

max_cals = []
cur_cals = 0

def compute_max(new_cals, max_cals):
    max_cals.append(new_cals)
    if len(max_cals) > 3:
        print("before" + str(max_cals))
        max_cals = sorted(max_cals, reverse=True)[:3]
        print("after" + str(max_cals))
    return max_cals

while True:
    line = f.readline()
    if not line:
        max_cals = compute_max(cur_cals, max_cals)
        cur_cals = 0
        break
    
    if line.strip() == "":
        max_cals = compute_max(cur_cals, max_cals)
        cur_cals = 0
        continue
    
    cur_cals += int(line)
    
    

f.close()

#print(max_cals)
result = sum(max_cals)

print(f"The # calories being carried by the top three elves is {result}.")