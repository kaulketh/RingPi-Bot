#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# bot
# created 01.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
import os
import signal
import time
from multiprocessing import Process

import telepot
from config import RING_BOT_TOKEN, RING_RING_GROUP, THK, \
    switch_state, \
    DING_DONG, WELCOME, RUNNING, STOPPED, UNKNOWN_CMD, UNKNOWN_TYPE, \
    RING_BOT_NAME, CMD_START, CMD_STOP, CMD_REBOOT, REBOOT, START, STARTED, \
    STOPPING
from bot import Singleton
from telepot.loop import MessageLoop

from logger import LOGGER


class RingBot(Singleton):
    """ Bot class using telepot framework
        (https://telepot.readthedocs.io),
        Python >= 3
    """

    def __init__(self, token, admin: list):
        self.__log = LOGGER
        self.__log.debug(f"Initialize instance of {self.__class__.__name__}")
        self.__token = token
        self.__admin = admin
        self.__bot = telepot.Bot(self.__token)
        self.__ding_dong = DING_DONG.format(RING_BOT_NAME)
        self.__receiver = RING_RING_GROUP
        self.__checker = None

    def __check_bell(self, timeout=.25):
        while True:
            if switch_state():
                self.__log.info(switch_state())
                self.__send(self.__receiver, self.__ding_dong)
            time.sleep(timeout)

    def __send(self, chat_id, text):
        self.__log.debug(
            f"Message posted: "
            f"{chat_id}|{text}".replace("\n", " "))
        self.__bot.sendMessage(chat_id, text)

    def __handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.__log.debug(msg)
        # check user
        if chat_id != self.__admin:
            # TODO: wrong id
            pass
            return
        # check content
        if content_type == 'text':
            command = msg['text']
            self.__log.info(f"Got command '{command}'")
            # commands
            # start
            if command == CMD_START:
                if self.__checker is None:
                    self.__checker = Process(target=self.__check_bell)
                    self.__checker.start()
                    self.__send(self.__admin, STARTED)
                self.__send(self.__admin, RUNNING)
            # stop
            elif command == CMD_STOP:
                if isinstance(self.__checker, Process):
                    self.__checker.terminate()
                    self.__checker = None
                    self.__send(self.__admin, STOPPING)
                self.__send(self.__admin, STOPPED)
            elif command == CMD_REBOOT:
                self.__send(self.__admin, REBOOT.format(RING_BOT_NAME))
                os.system("sudo reboot")
            else:
                self.__send(self.__admin, UNKNOWN_CMD)
        else:
            self.__send(self.__admin, UNKNOWN_TYPE)

    def start(self):
        try:
            MessageLoop(self.__bot,
                        {'chat': self.__handle}).run_as_thread()
            self.__log.info(START)
            self.__send(self.__admin, WELCOME.format(RING_BOT_NAME))
            while True:
                try:
                    signal.pause()
                except KeyboardInterrupt:
                    self.__log.warning('Program interrupted')
                    exit()
        except Exception as e:
            self.__log.error(f"An error occurred: {e}")
            exit()


def run():
    RingBot(RING_BOT_TOKEN, THK).start()


if __name__ == '__main__':
    pass
