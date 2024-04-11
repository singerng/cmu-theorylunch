"""This script trims a video and attaches a title page to it

By default, if the video file is videofile.mp4, then the script expects the 
title picture to be videofile.png, and will output the video to 
videofile-cut.mp4.

These can be changed by the flags --title-file and --output-file respectively.

Example:
  python cut.py videofile.mp4 1:05 1:02:15

Author: Brian Zhang <bhzhang@cs.cmu.edu>
"""

import argparse
import os
import sys

def time(s):
	return sum(x * float(t) for x, t in zip([1, 60, 3600], reversed(s.split(":"))))

parser = argparse.ArgumentParser()
parser.add_argument("video_file", type=str)
parser.add_argument("start_time", type=time)
parser.add_argument("end_time", type=time)

parser.add_argument("--title-file", type=str, default=None)
parser.add_argument("--title-duration", type=int, default=4)
parser.add_argument("--output-file", type=str, default=None)

args = parser.parse_args()

basename = os.path.splitext(args.video_file)[0]

if args.output_file is None: args.output_file = basename + "-cut.mp4"
if args.title_file is None: args.title_file = basename + ".png"

if os.path.exists(args.output_file):
	res = input("Overwrite file %s [y/n]? " % args.output_file)
	if not "y" in res: sys.exit(0)

from moviepy.editor import *



clip = VideoFileClip(args.video_file)
clip = clip.subclip(args.start_time, args.end_time)

title = ImageClip(args.title_file, duration=args.title_duration)
size = min(clip.size[0]/title.size[0], clip.size[1]/title.size[1])
print("resizing to", size)
title = title.resize(float(size))
print("new size:", title.size)

clip = concatenate_videoclips([title, clip], method="compose")

clip.write_videofile(args.output_file, temp_audiofile='temp-audio.mp4', remove_temp=True, codec='libx264', audio_codec='aac')
