#For each click variable, calculate the temperature and print it as shown in the instructions
temp = 40


def temp_adjustment(temp, clicks):
    temp = clicks + temp
    lowest_temp = 40
    highest_temp = 89
    temp_diff = highest_temp - lowest_temp + 1

    while temp > 89:
        temp = temp - temp_diff

    while temp < 40:
        temp = temp + temp_diff

    print("The temperature is", temp)


click_1 = 0
temp_adjustment(temp, click_1)

click_2 = 49
temp_adjustment(temp, click_2)

click_3 = 74
temp_adjustment(temp, click_3)

click_4 = 51
temp_adjustment(temp, click_4)

click_5 = -1
temp_adjustment(temp, click_5)

click_6 = 200
temp_adjustment(temp, click_6)
