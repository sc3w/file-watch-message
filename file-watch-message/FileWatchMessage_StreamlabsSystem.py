#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""Redeem script to redeem rewards for a cost for users"""
#---------------------------------------
# Libraries and references
#---------------------------------------
import os
import sys
import json
import re
import time
import math
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import codecs
import ctypes

from Settings_Module import MySettings

#---------------------------------------
# [Required] Script information
#---------------------------------------
ScriptName = "File Watch Message"
Website = ""
Creator = "Sc3w"
Version = "1.0.0"
Description = "File watch message"
#---------------------------------------
# Versions
#---------------------------------------
"""
1.0.0 Script made.
"""
#---------------------------------------
# Variables
#---------------------------------------
global SettingsFile
SettingsFile = ""

global ScriptSettings
ScriptSettings = None

global TimerTick
TimerTick = None

#---------------------------------------
# System functions
#---------------------------------------

#---------------------------------------
# [Required] functions
#---------------------------------------

def Init():
    global ScriptSettings
    path = os.path.dirname(__file__)

    # Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")

    ScriptSettings = MySettings(SettingsFile)

    ScriptSettings.Initialized = True

    return

def Execute(data):
    #I wanna be the very best
    #Like no one ever was
    #To catch them is my real test
    #To train them is my cause
    return

def Tick():
    global TimerTick
    global ScriptSettings

    if ScriptSettings is None:
        return

    if not ScriptSettings.Initialized:
        return

    if TimerTick is None:
        TimerTick = time.time()

    if (time.time() - TimerTick):
        TimerTick = time.time()
        Watch()

    return

def Watch():
    path = os.path.dirname(__file__)
    with codecs.open(os.path.join(path, 'message.txt'), encoding='utf-8-sig', mode='r') as f:
        data = f.read()
        if len(data) > 0:
            Parent.SendTwitchMessage(ScriptSettings.Message.format(data))
            with codecs.open(os.path.join(path, 'message.txt'), encoding='utf-8-sig', mode='w+') as file:
                file.write('')