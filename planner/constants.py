import calendar


def weekdays():
    day_names = [n.lower() for n in calendar.day_name]
    return day_names


def one_hot_encoded_weekdays():
    week_days_list = weekdays()
    #  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    one_hot_array = [1, 1, 0, 1, 1, 1, 0]
    return list(zip(week_days_list, one_hot_array))
