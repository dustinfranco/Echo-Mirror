#!/bin/bash

#Take picture
mv ./pics/out.png ./pics/out_last.png
xrandr --output DP-1 --brightness 1.0
ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -ss 0:0:01 -frames 1 ~/echo-mirror/ubuntu/pics/out.png -y
ffmpeg -i ~/echo-mirror/ubuntu/pics/out.png -vf transpose=0 ~/echo-mirror/ubuntu/pics/out.png -y

#Analyze picture
number_faces=`python face_detect_cv3.py`


#no faces, return to beginning
if [ "$number_faces" -eq 0 ]; then
  echo "no faces"

#found faces
else
  #start recording
  echo "faces found: $number_faces"
      #to disable eye of gnome animations:
      #gsettings set org.gnome.desktop.interface enable-animations false
  
  #Kill any other images 
  kill `ps -ef| grep eog | awk '{print $2}'`
  #obligatory "it doesn't work without a sleep"
  sleep 0.1 
  #Display new image
  eog --fullscreen ./pics/out.png &
  
  #TODO: start recording now

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

  #TODO: grayscale video
  #TODO: replace old recording with new recording

  kill `ps -ef| grep eog | awk '{print $2}'`
  eog --fullscreen ./pics/black.png &
  xrandr --output DP-1 --brightness 1.0
  kill `ps -ef| grep eog | awk '{print $2}'`
fi


