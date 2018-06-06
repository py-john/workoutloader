#!/usr/bin/env python3
'''workout.py
   Opens a different video file for a daily
   workout based on a workout calendar.
'''
from time import sleep
from datetime import datetime, date
import create

PROGRAM_START_DATE = datetime(2018, 3, 19, 4, 30)


def print_calendar(day):
    '''Draws a calendar with X's for completed days'''
    print()
    for d in range(1, 91):
        text = d
        if d < day:
            text = 'X'
        print(str(text).rjust(2), end=' ')
        if d % 7 == 0:
            print()
        if d < 60 and d % 28 == 0:
            print()

    if day > 90:
        print('\n\n----Elite  Block----\n')
        for d in range(1, 28):
            text = d
            if d < (day-91):
                text = 'X'
            print(str(text).rjust(2), end=' ')
            if d % 7 == 0:
                print()


def main():
    workouts = create.workout_list()
    # find workout for current day
    now = datetime.now()
    day_number = (now - PROGRAM_START_DATE).days + 1

    workout = None
    for w in workouts:
        if day_number in w.days:
            workout = w
            break

    # Draw calander
    print_calendar(day_number)

    # Open and maximize workout video
    if workout:
        print('\n\nDay:', day_number)
        print(workout, '\n')
        sleep(2)
        workout.load_image()
        workout.load_video()


if __name__ == '__main__':
    main()
