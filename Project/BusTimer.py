def bus_timer(current_time):
    time = int(current_time[0:2]) * 60 + int(current_time[3:5])

    if time + 5 > 1440:
        return 1440 - time + 355

    if time < 355:
        return 355 - time

    return (10 - time % 15) % 15

print(15 - 370 % 15)
