#!/bin/bash
echo "beginning echo mirror"
mv ./pics/out.png ./pics/out_last.png
xrandr --output DP-1 --brightness 1.0
ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -ss 0:0:01 -frames 1 ~/echo-mirror/ubuntu/pics/out.png -y
ffmpeg -i ~/echo-mirror/ubuntu/pics/out.png -vf transpose=2 ~/echo-mirror/ubuntu/pics/out.png -y
number_faces=`python face_detect_cv3.py`
if [ "$number_faces" -gt 0 ]; then
  echo "faces found: $number_faces"
else
  echo "no faces"
fi


