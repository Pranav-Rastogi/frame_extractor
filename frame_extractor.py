import os
import sys
import shutil
import argparse
import subprocess


# Get command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--file', help='Path to the video file that needs to be read.')
parser.add_argument('--frames', help='Number of frames per second.', nargs='?', const=10, default=10)
args = parser.parse_args()


# Preparing directory for saving frames
try:
    if os.path.exists('frames'):
        try:
            shutil.rmtree('frames')
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            sys.exit()

    os.makedirs('frames')
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))
    sys.exit()


dest = "frames/video_%02d.jpg"


# DO NOT TOUCH!
command = 'ffmpeg -i "{}" -r {} -q:v 1 {}'.format(args.file, args.frames, dest)
pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out, err = pipe.communicate()
