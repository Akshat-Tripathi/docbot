# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:41:45 2020

@author: Akshat
"""

from mouse import move, click
from keyboard import press_and_release
from selenium import webdriver
from time import sleep

TICKET_ID = "-89040641957"
X, Y = 600, 270
DELTA_Y = 100

REG_X, REG_Y = 600, 750

def click_select(n):
    move(X, Y + n * DELTA_Y)
    click()

driver = webdriver.Chrome()
driver.get("https://www.eventbrite.co.uk/e/hackhack-tickets" + TICKET_ID)
reg1 = driver.find_element_by_id("eventbrite-widget-modal-trigger" + TICKET_ID)
reg1.click()
sleep(2)
click_select(0)
press_and_release("down")
press_and_release("enter")
sleep(2)
move(REG_X, REG_Y)
click()