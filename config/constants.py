#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# constants
# created 01.10.2021
# Thomas Kaulke, kaulketh@gmail.com
# https://github.com/kaulketh
# -----------------------------------------------------------
CHECK_NAME = "Klingel-Überwachung"

CMD_START = "/start"
CMD_STOP = "/stop"
CMD_REBOOT = "/reboot"

UNKNOWN_CMD = "UNKNOWN COMMAND!"
UNKNOWN_TYPE = "UNKNOWN CONTENT TYPE!"

REBOOT = "{} wird neu gestarte!"
START = "Bot is running..."
WELCOME = "{} einsatzbereit!\n Starten mit '/start'!"

STARTED = f"{CHECK_NAME} gestartet."
RUNNING = f"{CHECK_NAME} läuft..."
STOPPING = f"{CHECK_NAME} wird angehalten."
STOPPED = f"{CHECK_NAME} gestoppt!"

DING_DONG = "{}\n\n\U0001F514 DING DONG \U0001F514\nEs hat an der Tür " \
            "geklingelt\U00002755"

# CMD_LIST_BOT_FATHER =
# start - Start Klingel-Check
# stop - Stop Klingel-Check
# reboot - Reboot Thk1220RingBot
