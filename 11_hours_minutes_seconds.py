'''
Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
argument for this parameter will be the number of seconds to be translated into the number of hours,
minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
function should return '10m' rather than '0h 10m 0s'. The only exception is that
getHoursMinutesSeconds(0) should return '0s'.
'''

def get_hours_min_sec(total_seconds):
    # calculating hours, minutes, seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # creating a list to store time components
    time_components = []

    # add hours, minutes and seconds to the list is it's greater than 0
    if hours > 0:
        time_components.append(f'{round(hours)}h')
    if minutes > 0:
        time_components.append(f'{round(minutes)}m')
    if seconds > 0 or total_seconds == 0:
        time_components.append(f'{round(seconds)}s')


    # join the components and return the result
    return ' '.join(time_components)


assert get_hours_min_sec(30) == '30s'
assert get_hours_min_sec(60) == '1m'
assert get_hours_min_sec(90) == '1m 30s'
assert get_hours_min_sec(3600) == '1h'
assert get_hours_min_sec(3601) == '1h 1s'
assert get_hours_min_sec(3661) == '1h 1m 1s'
assert get_hours_min_sec(90042) == '25h 42s'
assert get_hours_min_sec(0) == '0s'

print(get_hours_min_sec(950))