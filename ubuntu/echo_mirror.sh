#!/bin/bash
echo "beginning echo mirror"
mv ./pics/out.png ./pics/out_last.png
xrandr --output DP-1 --brightness 1.0
ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -ss 0:0:01 -frames 1 ~/echo-mirror/ubuntu/pics/out.png -y
ffmpeg -i ~/echo-mirror/ubuntu/pics/out.png -vf transpose=2 ~/echo-mirror/ubuntu/pics/out.png -y
number_faces=`python face_detect_cv3.py`
if [ "$number_faces" -gt 0 ]; then
  echo "faces found: $number_faces"
  #to disable eye of gnome animations:
  #gsettings set org.gnome.desktop.interface enable-animations false
  
  #Display Image
  eog --fullscreen ./pics/out.png &
  
  #Fade screen on
  for i in $(seq 0 0.01 1)
  do
    xrandr --output DP-1 --brightness $i
  done
  sleep 3.0
  
  #Fade sreen off
  for m in $(seq 0 0.01 1)
  do
    brightness=$(bc<<<1.0-$m)
    #echo $brightness
    xrandr --output DP-1 --brightness $brightness
  done

  xrandr --output DP-1 --brightness 1.0

else
  echo "no faces"
fi


