import os
import sys
import requests
from IPython.display import Audio
from sys import argv  # For accessing the commandline
# More about the libary: https://pytube.io/en/latest/
from pytube import YouTube, Playlist

# on_progress_callback takes 4 parameters.
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
    percent = (100*(file_size-remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))
    
def link_checking(link):
    r = requests.get(link)
    return "Video unavailable" in r.text


if len(argv) == 2:
    link = argv[1]  # To take the input from the terminal.

elif len(argv) == 1:
    print("Waiting for video link: ", end=" ")
    link = input()

# checking the link is valid or not
if link_checking(link):
    print("Video is not availale")
else:
    try:
        yt = YouTube(link)
        title= yt.title
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Publish data: ", yt.publish_date)

        print("Do want to download the video 🤫")
        option = input()
        option.lower()
        if 'y' in option or 'yes' in option or 'hmm' in option:
            yt_downloder = yt.streams.get_highest_resolution()
            yt_downloder.download(".\downloaded")
    # 🔜 Audio download will be added.

        else:
            print("✌🏻 Peace Out ✌🏻")
    except:
        print("Oops! 😮", sys.exc_info()[0], "occurred.")
        print("Check You Link... 🔗🔗")
