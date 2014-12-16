#!/usr/bin/env python3

'''
微信头像未读提醒样式
'''

from PIL import Image, ImageDraw, ImageFont

image = Image.open('../ref/pic.jpg')
width, height = image.size
font_size = height // 6
font = ImageFont.truetype("../ref/Verdana.ttf", font_size)

draw = ImageDraw.Draw(image)
text = '999'
text_width, text_height = draw.textsize(text, font=font)
draw.text((width - text_width, 0), text, fill=(255, 0, 0), font=font)

image.show()
# image.save("../ref/result.jpg")
