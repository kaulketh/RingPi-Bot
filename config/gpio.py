#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# gpio
# created 01.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import RPi.GPIO as GPIO

PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)


def switch_state():
    return False if GPIO.input(PIN) == 0 else True


if __name__ == '__main__':
    pass
