import common as cm
import cv2
import numpy as np
from PIL import Image
import time
from threading import Thread

import sys
sys.path.insert(0, '/var/www/html/earthrover')
import util as ut
ut.init_gpio()

bject_to_track='person'

#---------Flask----------------------------------------
from flask import Flask, Response
from flask import render_template
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme

#---------import 2 ----------------------------------------
