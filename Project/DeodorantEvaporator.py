def evaporator(content, evap_per_day, threshold):
    threshold = threshold * content / 100
    days = 0
    while content > threshold:
        content -= content * evap_per_day / 100
        days += 1

    return days
