weekly_optimal = input()
dishes = []
while(1):
    dish = raw_input()
    if not dish:
        break
    dishes.append((int(dish.split(' = ')[1]), dish.split(' = ')[0]))
dishes = sorted(dishes)
daily_optimal = weekly_optimal/7
index_determination = [i for i, dish in enumerate(dishes) if dish[0] == daily_optimal]
calorie_less = []
calorie_equal = []
calorie_greater = []
if len(index_determination) == 0:
    pivot = -1
    for dish in dishes:
        if dish[0] < daily_optimal:
            pivot += 1
    calorie_less = dishes[0:pivot + 1]
    calorie_greater = dishes[pivot + 1:]
else:
    calorie_less = dishes[0: index_determination[0]]
    calorie_equal = dishes[index_determination[0]: index_determination[-1] + 1]
    calorie_greater = dishes[index_determination[-1] + 1:]
selected_dishes = [dish for i, dish in enumerate(calorie_equal) if i < 7]
calorie_offset = 0
while(len(selected_dishes) < 7):
    differences_calorie_less = map(lambda x: (abs((x[0] + calorie_offset) - daily_optimal), x), calorie_less)
    differences_calorie_greater = map(lambda x: (abs((x[0] + calorie_offset) - daily_optimal), x), calorie_greater)
    try:
        min_diff_calorie_less = min(differences_calorie_less)
    except:
        min_diff_calorie_less = (100000000000000000000, (0, "Just a placeholder"))
    try:
        min_diff_calorie_greater = min(differences_calorie_greater)
    except:
        min_diff_calorie_greater = (100000000000000000000, (0, "Just a placeholder"))
    if min_diff_calorie_less[0] < min_diff_calorie_greater[0]:
        index = differences_calorie_less.index(min_diff_calorie_less)
        selected_dishes.append(min_diff_calorie_less[1])
        calorie_less = calorie_less[0:index] + calorie_less[index + 1:]
        calorie_offset = min_diff_calorie_less[1][0] + calorie_offset - daily_optimal
    else:
        index = differences_calorie_greater.index(min_diff_calorie_greater)
        selected_dishes.append(min_diff_calorie_greater[1])
        calorie_greater = calorie_greater[0:index] + calorie_greater[index + 1:]
        calorie_offset = min_diff_calorie_greater[1][0] + calorie_offset - daily_optimal
total_calorie = 0
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i, dish in enumerate(selected_dishes):
    total_calorie += dish[0]
    print('%s: %s' % (week_days[i], dish[1]))
print('Total: %d kcal, out of %d kcal required' % (total_calorie, weekly_optimal))
