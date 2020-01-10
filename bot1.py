# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:41:45 2020

@author: Akshat
"""

from mouse import move, click
from keyboard import press_and_release
from selenium import webdriver
from pause import until, datetime, sleep
import timeit


# TICKET_ID = "-89040641957" # HACKHACK
# TICKET_ID = "-89217230137" # HACK1040
# TICKET_ID = "-89221236119" #TEST
TICKET_ID = "-81611641617"

X, Y = 600, 270
DELTA_Y = 100
# URL = "https://www.eventbrite.co.uk/e/hackhack-tickets"
# URL = "https://www.eventbrite.co.uk/e/hack1040-tickets"
# URL = "https://www.eventbrite.co.uk/e/test-tickets"
URL = "https://www.eventbrite.co.uk/e/ic-hack-20-tickets"
# LAUNCH = datetime(2020, 1, 10, 13, 30, 0, 100000)
LAUNCH = datetime(2020, 1, 10, 13, 29, 59, 100000)

REG_X, REG_Y = 600, 750

def click_select(n):
    move(X, Y + n * DELTA_Y)
    click()

driver = webdriver.Chrome()

until(LAUNCH)
s = timeit.default_timer()
driver.get(URL  + TICKET_ID)
load = timeit.default_timer()
reg1 = driver.find_element_by_id("eventbrite-widget-modal-trigger" + TICKET_ID)
reg1.click()
sleep(2)
click_select(0)
press_and_release("down")
press_and_release("enter")
sleep(1)
move(REG_X, REG_Y)
click()
e = timeit.default_timer()
print(load - s)
print(e - load)