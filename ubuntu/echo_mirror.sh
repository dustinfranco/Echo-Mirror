#!/bin/bash
mkdir ~/starting
#eog --fullscreen ~/echo-mirror/pics/black.png &
while :
do
  #rm /home/phnx/echo-mirror/ubuntu/pics/test.png
  #xrandr --output DP-1 --brightness 0.0
  #Take picture
  ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -ss 0:0:01 -frames 1 ~/echo-mirror/ubuntu/pics/out_new.png -y
  ffmpeg -i ~/echo-mirror/ubuntu/pics/out_new.png -vf transpose=0 ~/echo-mirror/ubuntu/pics/out.png -y

  #Analyze picture
  #number_faces=`python face_detect_cv3.py`
  python face_detect_cv3.py
  number_faces=$?

  #no faces, return to beginning
  if [ "$number_faces" -eq 0 ]; then
    wall "no faces"

  #found faces
  else
    #start recording
    wall "faces found: $number_faces"
        #to disable eye of gnome animations:
        #gsettings set org.gnome.desktop.interface enable-animations false
    
    #Kill any other images 
    kill `ps -ef| grep eog | awk '{print $2}'`
    #obligatory "it doesn't work without a sleep"
    sleep 0.1 
    #Display new image
    #nice -n -3 eog --fullscreen ./pics/out.gif &
    mplayer -fs ~/echo-mirror/ubuntu/pics/out.gif &
    sleep 1.0
    
    #TODO: start recording now

    ffmpeg -f video4linux2 -s 1280x720 -i /dev/video0 -t 15 ~/echo-mirror/ubuntu/pics/out_new.gif -y  &
    #sleep 10.0
    #Fade `screen on
    for i in $(seq 0 0.01 1)
    do
      xrandr --output DP-1 --brightness $i
    done
    sleep 9.0
    
    #Fade sreen off
    for m in $(seq 0 0.01 1)
    do
      brightness=$(bc<<<1.0-$m)
      #echo $brightness
      xrandr --output DP-1 --brightness $brightness
    done

    #TODO: grayscale video
    #TODO: replace old recording with new recording'
    #ffmpeg -i ~/echo-mirror/ubuntu/pics/out_new.gif -t 15 -vf transpose=0 ~/echo-mirror/ubuntu/pics/out_new_2.gif -y
    ffmpeg -i ~/echo-mirror/ubuntu/pics/out_new.gif -vf hflip -c:a copy ~/echo-mirror/ubuntu/pics/out_new_2.gif -y

    #ffmpeg -i ~/echo-mirror/ubuntu/pics/out_new.gif -t 15 -vf transpose=2 ~/echo-mirror/ubuntu/pics/out_new_2.gif -y
    ffmpeg -i ~/echo-mirror/ubuntu/pics/out_new_2.gif -t 15 -vf hue=s=0 ~/echo-mirror/ubuntu/pics/out.gif -y
    #gifsicle -O3 ~/echo-mirror/ubuntu/pics/out_new.gif ~/echo-mirror/ubuntu/pics/out.gif

    #kill `ps -ef| grep eog | awk '{print $2}'`
    #eog --fullscreen ~/echo-mirror/ubuntu/pics/test.png &
    #kill `ps -ef| grep eog | awk '{print $2}'`
    
    #xrandr --output DP-1 --brightness 1.0
    #echo "kill me now"
    #sleep 5.0
    #xrandr --output DP-1 --brightness 0.0
  fi
done


