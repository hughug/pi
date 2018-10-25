#!/usr/bin/python
# -*- coding: utf-8 -*-
# monitor app for raspberry pi using waveshare 1.54in e-ink display
# Baoyi Chen 2018

import epd1in54
import time
from PIL import Image,ImageFont,ImageDraw
from cputemp import *

deg=u'\xb0'

def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    draw.rectangle((0,0,epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), fill = 255)
    #draw.text((20, 12), 'Hello world!', font = font, fill = 255)
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    #epd.delay_ms(2000)

    # for partial update
    epd.init(epd.lut_partial_update)
    #image = Image.open('monocolor.bmp')
##
 # there are 2 memory areas embedded in the e-paper display
 # and once the display is refreshed, the memory area will be auto-toggled,
 # i.e. the next action of SetFrameMemory will set the other memory area
 # therefore you have to set the frame memory twice.
 ##     
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()

    time_image = Image.new('1', (120, 120), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(time_image)
    font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 32)
    image_width, image_height  = time_image.size
    while (True):
        # draw a rectangle to clear the image
        draw.rectangle((0, 0, image_width, image_height), fill = 255)
        localtime = time.strftime("%H:%M")
        cputemp   = '%.1f'%gettemp()+'°C'[1:]
        draw.text((8,  0), '%s'%cputemp,   font = font1, fill = 0)
        draw.text((0, 30), '%s'%localtime, font = font2, fill = 0)
        epd.set_frame_memory(time_image, 80, 80)
        epd.display_frame()
        epd.delay_ms(2000)

if __name__ == '__main__':
    main()
