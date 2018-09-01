#!/bin/bash
echo "beginning echo mirror"
ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -ss 0:0:01 -frames 1 ~/echo-mirror/ubuntu/pics/out.png -y
ffmpeg -i ~/echo-mirror/ubuntu/pics/out.png -vf transpose=2 ~/echo-mirror/ubuntu/pics/out.png -y


