#!/usr/bin/env python3

import time, random
import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, SpeedRPM, SpeedPercent, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sound import Sound


class EV3rstorm:

    def __init__(self):
        '''Подготовить все устройства'''
        print('Init robot ...')

        self.screen = ev3.Screen()
        self.sound = Sound()
        
        self.lm = LargeMotor(OUTPUT_B)
        self.rm = LargeMotor(OUTPUT_C)
        self.steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

        self.draw_face()
        self.sound.speak('Hello!')

    def move_forward(self, spc, n):
        '''Движение вперед'''
        self.steer_pair.on_for_rotations(
            0, SpeedPercent(spc), n)

    def draw_face(self):
        '''Нарисовать глаза на экране'''
        w,h = self.screen.shape
        y = h // 2

        eye_xrad = 20
        eye_yrad = 30

        pup_xrad = 10
        pup_yrad = 10

        def draw_eye(x):
            self.screen.draw.ellipse((x-eye_xrad, y-eye_yrad, x+eye_xrad, y+eye_yrad))
            self.screen.draw.ellipse((x-pup_xrad, y-pup_yrad, x+pup_xrad, y+pup_yrad), fill='black')

        draw_eye(w//3)
        draw_eye(2*w//3)

        self.screen.update()

if __name__ == '__main__':
    Beaver = EV3rstorm()
    Beaver.move_forward(50, 10)