import os
import subprocess
from time import sleep
import pyautogui

class Workout(object):
    '''Defines the workout with days to be done and
       relavant file paths.
    '''
    def __init__(self, name, days, video_file, image_file=None):
        self.name = name
        self.days = days
        self.video_file = video_file
        self.image_file = image_file

    def load_video(self):
        subprocess.Popen(['open', self.video_file])
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


def workout_list():
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

    return workouts
