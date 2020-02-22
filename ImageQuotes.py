#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import math

from PIL import Image, ImageDraw, ImageFont

# create font object with the font file and specify
# desired size
# create Image object with the input image

image = Image.open('main.png')

# initialise the drawing context with
# the image object as background

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('san_francisco.otf', size=45)
font_author = ImageFont.truetype('san_francisco.otf', size=33)

font_ligth = ImageFont.truetype('san_francisco_light.otf', size=45)


# starting position of the message
print image.width
print image.height
(x, y) = (150, image.height/1.766)

message = "If you make a great number of predictions, the ones that were wrong will soon be forgotten, and the ones that turn out to be true will make you famous."
message1 = "Practice isn’t the thing you do once you’re good. It’s the thing you do that makes you good."
message2 = "We have, as human beings, a storytelling problem. We’re a bit too quick to come up with explanations for things we don’t really have an explanation for."
author= "creatorscms.com"
message1=message1.decode('utf-8').strip()
message2=message2.decode('utf-8').strip()

i = 1
message_with_returns="";
temp_message = message2
final_message=""
ch_count=0
messageA = []
strln=len(temp_message)

#104/26 = 4
theCut=26
while strln>=0:
  if strln<=26:
    messageA.append(temp_message[0:])
    strln=0
    break
  else:

  #message_with_returns +=  temp_message + "\n"
  #print(message_with_returns)
    temp = temp_message[theCut:len(temp_message)]
    print (temp)
    print(i)
    try:
      cut = theCut + temp.index(" ")
    except:
      cut=26

    messageA.append(temp_message[0:cut])

    temp_message= temp_message[cut:len(temp_message)]
    strln=len(temp_message)
    print(str(strln)+"strln")

message_final=""
for o in messageA:
    print o
    message_final += o + "\n"

color = 'rgb(244, 244, 244)' # black color

# draw the message on the background

draw.text((x, y), message_final, fill=color, font=font_ligth)
(x, y) = (150, image.height-66)

name = '-Malcolm Gladwell'
color = 'rgb(255, 255, 255)' # white color
draw.text((x, y), name, fill=color, font=font)

(x, y) = (image.width/1.5, image.height-56)

name = author
color = 'rgb(255, 255, 255)' # white color
draw.text((x, y), name, fill=color, font=font_author)


# save the edited image

image.save('greeting_card.png')