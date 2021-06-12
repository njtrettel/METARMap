import time
import datetime
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
image = image.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)
draw = ImageDraw.Draw(image)

# Black box to clear image
def clear():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)

# Load font
font = ImageFont.truetype('font.ttf', 24)
font_emoji = ImageFont.truetype('emoji.ttf', 16)
font_emoji_large = ImageFont.truetype('emoji.ttf', 24)

# while True:
clear()
draw.text((0, -4), datetime.datetime.now().strftime('%a %H:%M'), font=font, fill=255)
draw.text((0, 12), '\U0001F4A8', font=font_emoji, fill=255)
draw.text((24, 12), '\U0001F44D', font=font_emoji, fill=255)
#draw.text((48, 12), '\U0001F440', font=font_emoji_large, fill=255)
draw.text((48, 12), '\u26C5', font=font_emoji, fill=255)
draw.text((72, 12), '\U0001F44E', font=font_emoji, fill=255)
disp.image(image.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT))
disp.show()
# time.sleep(0.5)
