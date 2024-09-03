"""
This script generates a title slide.

Author: Noah Singer <ngsinger@cs.cmu.edu>
Python implementation of GIMP image template by Brian Zhang <bhzhang@cs.cmu.edu>

Usage: update the SEMESTER_TEXT and SEMESTER_BLOCK_COLOR variables each semester.
After running, the title slide image will be displayed (e.g. in Preview on Mac) and can be saved.
"""

from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFont

title_lines = []
while True:
    line = input("Title line (empty to stop): ")
    if not line:
        break
    title_lines.append(line)
title_text = "\n".join(title_lines)
author_text = input("Presenter: ")
date_text = input("Date (e.g., 10 Apr 2024): ")
semester_name_text = input("Semester (e.g., Spring 2024): ")
semester_color_r = int(input("Semester color, R (in hex): "), 16)
semester_color_g = int(input("Semester color, G (in hex): "), 16)
semester_color_b = int(input("Semester color, B (in hex): "), 16)

img = Image.open("title_slide_template.png")
draw = ImageDraw.Draw(img)

IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080

BLACK = (0, 0, 0)
RED = (semester_color_r, semester_color_g, semester_color_b)

TITLE_COLOR = BLACK
TITLE_FONT_SIZE = 87
TITLE_FONT_NAME = "Helvetica"
TITLE_FONT_IDX = 1 # bold
TITLE_X = 990
TITLE_Y = 460
TITLE_INTRALINE_PAD = 30

title_font = ImageFont.truetype(TITLE_FONT_NAME, TITLE_FONT_SIZE, index=TITLE_FONT_IDX)
draw.multiline_text((TITLE_X, TITLE_Y), title_text, font=title_font, fill=TITLE_COLOR, spacing=TITLE_INTRALINE_PAD, align="center", anchor="ma")

AUTHOR_COLOR = BLACK
AUTHOR_FONT_SIZE = 55
AUTHOR_FONT_NAME = "Helvetica"
AUTHOR_FONT_IDX = 1 # bold
AUTHOR_X = 130
AUTHOR_Y = 980

author_font = ImageFont.truetype(AUTHOR_FONT_NAME, AUTHOR_FONT_SIZE, index=AUTHOR_FONT_IDX)
draw.text((AUTHOR_X, AUTHOR_Y), author_text, font=author_font, fill=AUTHOR_COLOR, align="left", anchor="lb")

DATE_COLOR = RED
DATE_FONT_SIZE = 55
DATE_FONT_NAME = "Helvetica"
DATE_FONT_IDX = 0 # normal
DATE_X = 1850
DATE_Y = 980

date_font = ImageFont.truetype(DATE_FONT_NAME, DATE_FONT_SIZE, index=DATE_FONT_IDX)
draw.text((DATE_X, DATE_Y), date_text, font=date_font, fill=DATE_COLOR, align="right", anchor="rb")

SEMESTER_COLOR = RED
SEMESTER_FONT_SIZE = 78
SEMESTER_FONT_NAME = "SIMPLIFICA Typeface"
SEMESTER_FONT_IDX = 0 # normal
SEMESTER_X = 1850
SEMESTER_Y = 250
SEMESTER_BLOCK_WIDTH = 70

SEMESTER_TEXT = "Theory Lunch - {}".format(semester_text)
SEMESTER_BLOCK_COLOR = (0xb4, 0xd3, 0xb2)

semester_font = ImageFont.truetype(SEMESTER_FONT_NAME, SEMESTER_FONT_SIZE, index=SEMESTER_FONT_IDX)
draw.text((SEMESTER_X, SEMESTER_Y), SEMESTER_TEXT, font=semester_font, fill=SEMESTER_COLOR, align="right", anchor="rs")

draw.rectangle([0, 0, SEMESTER_BLOCK_WIDTH, IMAGE_HEIGHT], fill=SEMESTER_BLOCK_COLOR)

img.show()
