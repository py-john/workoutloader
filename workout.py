#!/usr/bin/env python3
''' workout.py
This program opens a different video file for a daily
workout depending on which day it is run.
'''
import os
import subprocess
import pyautogui
from time import sleep
from datetime import datetime, date

PROGRAM_START_DATE = datetime(2018, 3, 19, 4, 30)
P90X_FOLDER = '/Users/john/Documents/P90X3/'


class Workout(object):
    ''' Workout class defines the workout with days to be done and
    relavant file paths.
    '''
    def __init__(self, name, days, video_file, image_file=None):
        self.name = name
        self.days = days
        self.video_file = video_file
        self.image_file = image_file

    def load_video(self):
        subprocess.Popen(['open', workout.video_file])
        os.system("osascript -e 'set Volume 2.9'")
        sleep(1.5)
        pyautogui.press('esc')
        pyautogui.hotkey('command', 'f')

    def load_image(self):
        if self.image_file:
            subprocess.Popen(['open', self.image_file])
            sleep(10)
            pyautogui.hotkey('command', 'w')

    def __str__(self):
        return self.name


# Draws calander with X's for completed days

def print_calendar(day):

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

    # define workouts and add to workouts list
    workouts = []

    total_synergistics = Workout(
            'Total Synergistics',
            [1, 8, 15, 64, 78],
            P90X_FOLDER + 'Total Synergistics.mp4',
            P90X_FOLDER + 'Total Synergistics.png')
    workouts.append(total_synergistics)

    agility_x = Workout(
            'Agility X',
            [2, 9, 16, 26, 65, 79, 113],
            P90X_FOLDER + 'Agility X.mp4')
    workouts.append(agility_x)

    x3_yoga = Workout(
            'X3 Yoga',
            [3, 10, 17, 27, 31, 38, 45, 55, 59, 66, 73, 80, 86, 94, 101, 108, 114],
            P90X_FOLDER + 'X3 Yoga.mp4')
    workouts.append(x3_yoga)

    the_challenge = Workout(
            'The Challenge',
            [4, 11, 18, 67, 81],
            P90X_FOLDER + 'The Challenge.mp4',)
    workouts.append(the_challenge)

    pilates_x = Workout(
            'Pilates X',
            [5, 12, 19, 25, 53, 68, 82, 97, 104, 111, 116],
            P90X_FOLDER + 'Pilates X.mp4')
    workouts.append(pilates_x)

    incinerator = Workout(
            'Incinerator',
            [6, 13, 20, 69, 83],
            P90X_FOLDER + 'Incinerator.mp4',
            P90X_FOLDER + 'Incinerator.png')
    workouts.append(incinerator)

    dynamix = Workout(
            'Dynamix',
            [7, 14, 21, 23, 28, 35, 42, 49, 51, 56, 63, 70, 77, 84, 90, 98, 105, 112, 118],
            P90X_FOLDER + 'Dynamix.mp4')
    workouts.append(dynamix)

    eccentric_upper = Workout(
            'Eccentric Upper',
            [29, 32, 36, 39, 43, 46, 57, 60, 71, 74, 89],
            P90X_FOLDER + 'Eccentric Upper.mp4')
    workouts.append(eccentric_upper)

    eccentric_lower = Workout(
            'Eccentric Lower',
            [30, 33, 37, 40, 44, 47, 58, 61, 72, 75, 88],
            P90X_FOLDER + 'Eccentric Lower.mp4')
    workouts.append(eccentric_lower)

    mmx = Workout(
            'MMX',
            [34, 41, 48, 62, 76],
            P90X_FOLDER + 'MMX.mp4')
    workouts.append(mmx)

    isometrix = Workout(
            'Isometrix',
            [22, 50, 85, 117],
            P90X_FOLDER + 'Isometrix.mp4')
    workouts.append(isometrix)

    the_warrior = Workout(
            'The Warrior',
            [24, 52],
            P90X_FOLDER + 'The Warrior.mp4')
    workouts.append(the_warrior)

    decelerator = Workout(
            'Decelerator',
            [54, 87],
            P90X_FOLDER + 'Decelerator.mp4')
    workouts.append(decelerator)

    complex_upper = Workout(
            'Complex Upper',
            [92, 95, 99, 102, 106, 109],
            P90X_FOLDER + 'Complex Upper.mp4')
    workouts.append(complex_upper)

    complex_lower = Workout(
            'Complex Lower',
            [93, 96, 100, 103, 107, 110],
            P90X_FOLDER + 'Complex Lower.mp4')
    workouts.append(complex_lower)

    ab_ripper = Workout(
            'Ab Ripper',
            [],
            P90X_FOLDER + 'Ab Ripper.mp4')
    workouts.append(ab_ripper)

    cvx = Workout(
            'CVX',
            [115],
            P90X_FOLDER + 'CVX.mp4')
    workouts.append(cvx)


    # find workout for current day
    now = datetime.now()
    day_number = (now - PROGRAM_START_DATE).days + 1

    workout = None
    for w in workouts:
        if day_number in w.days:
            workout = w
            break

    # Check for days with 2 workouts
    if workout == complex_upper:
        option = None
        print('1) Ab Ripper     2) Complex Upper')
        while(option not in ['1', '2']):
            option = input('> ')
        if option == '1':
            workout = ab_ripper

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
