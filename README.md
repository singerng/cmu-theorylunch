A collection of scripts and instructions for maintaining the YouTube channel and website for the CMU CS Theory Lunch, as well as general instructions for organizing the lunch.

## AUTHORS

- Brian Zhang (@brianhzhang)
- Noah Singer (@singerng)

## HOWTO

This repository contains scripts for making recorded videos into YouTube videos. There are two tasks:

1. Creating a title slide image.
2. Editing the title slide into the video.

At the beginning of the semester, please pick a color to use for all the YouTube title slides for the semester. This color will be encoded as an HTML color: `<red_hex> <green_hex> <blue_hex>`. A reference might be [https://htmlcolorcodes.com].

You will need to install a font called `SIMPLIFICA Typeface`, which you can find for free online.

The scripts require two libraries, `Pillow` and `moviepy`. As of Spring 2024, we used versions `9.5.0` and `1.0.3` respectively of the packages. (`moviepy` doesn't appear to work with the latest version of `Pillow`.) You can install these with the commands:

`pip install pillow==9.5.0`
`pip install moviepy==1.0.3`

### Creating the title slide

Enter the `title_slide` subdirectory and run `python title_slide.py`. You will see a series of prompts for the title, presenter, date, and semester, as well as the semester color. When these prompts finish, the script will open a temporary image file on your computer, which you should then save in the repository's *root* directory as `<name>.png` where <name> is some unique name for the video. The prompts accept linebreaks; you may need to play around with where to put the linebreaks to get a good-looking title slide.

### Exporting the video

From the *root* directory, run `python cut/cut.py <name>.mov <hr_start>:<min_start>:<hr_start> <hr_end>:<min_end>:<sec_end>`. The script expects the uncut video file in the root directory as `<name>.mov` (upload it here from your phone or wherever you recorded it) and the title slide in the root directory as `<name>.png`, and will produce a cut and titled video file with name `<name>-cut.mp4`. `<hr_start>:<min_start>:<sec_start>` and `<hr_end>:<min_end>:<sec_end>` are *timestamps* in the uncut video for when you want the cut video to start and stop, allowing you to e.g. truncate the video if it started too early or ended too late.
