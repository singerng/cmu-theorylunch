A collection of scripts and instructions for maintaining the YouTube channel and website for the CMU CS Theory Lunch, as well as general instructions for organizing the lunch.

## AUTHORS

- Brian Zhang (@brianhzhang)
- Noah Singer (@singerng)

## HOWTO

This repository contains scripts for making recorded videos into YouTube videos. There are two tasks:

1. Creating a title slide image.
2. Editing the title slide into the video.

### Creating the title slide

Enter the `title_slide` subdirectory and run `python title_slide.py`. You will see a series of prompts for the title, author, date, and semester. When these prompts finish, the script will open a temporary image file on your computer, which you should then save in the repository's *root* directory as `<name>.png` where <name> is some unique name for the video. The prompts accept linebreaks; you may need to play around with where to put the linebreaks to get a good-looking title slide.

This script requires Pillow, a Python image processing library.

### Exporting the video

From the *root* directory, run `python cut/cut.py <name>.mov <hr_start>:<min_start>:<hr_start> <hr_end>:<min_end>:<sec_end>`. The script expects the uncut video file in the root directory as `<name>.mov` (upload it here from your phone or wherever you recorded it) and the title slide in the root directory as `<name>.png`, and will produce a cut and titled video file with name `<name>-cut.mp4`. `<hr_start>:<min_start>:<sec_start>` and `<hr_end>:<min_end>:<sec_end>` are *timestamps* in the uncut video for when you want the cut video to start and stop, allowing you to e.g. truncate the video if it started too early or ended too late.

This script requires <what?>
