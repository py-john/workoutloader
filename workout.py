#!/usr/bin/env python3
"""workout.py:
   Opens video files for daily workouts based on a workout calendar.
"""
from time import sleep
from datetime import datetime
import create

PROGRAM_START_DATE = datetime(2019, 1, 7, 5, 0)


def print_calendar(day):
    """Draws a calendar with X's for completed days"""
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


def get_day():
    """Return the number of the current day in the schedule"""
    return ((datetime.now() - PROGRAM_START_DATE).days + 1)


def get_workout(day_number):
    """Return workout object for current day"""
    workouts = create.workout_list()
    workout = None
    for w in workouts:
        if day_number in w.days:
            workout = w
            break
    return workout


def main():
    """Get the workout for the current day and load the image/video files"""
    day_number = get_day()
    workout = get_workout(day_number)
    print_calendar(day_number)
    if workout:
        print('\n\nDay:', day_number)
        print(workout, '\n')
        sleep(2)
        workout.load_image()
        workout.load_video()


if __name__ == '__main__':
    main()
