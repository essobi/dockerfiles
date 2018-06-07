# Build with:  
# docker build --rm -t everbot/firefox .  
  
# Run with:  
# XSOCK=/tmp/.X11-unix  
# XAUTH=/tmp/.docker.xauth  
# xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -  
# docker run -ti \  
# -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# \--device /dev/snd:/dev/snd \  
# -v $HOME/.spotify/config:/home/spotify/.config/spotify \  
# -v $HOME/.spotify/cache:/home/spotify/spotify \  
# \--name spotify \  
# everbot/spotify bash  
  
# docker run -ti --rm \  
# -v $XAUTH:$XAUTH -e XAUTHORITY=$XAUTH \  
# -e DISPLAY=$DISPLAY \  
# \--device /dev/snd:/dev/snd \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# everbot/firefox bash  
  
FROM everbot/archlinux-basic  
  
RUN sudo pacman -Syy  
  
RUN sudo pacman --noconfirm -S firefox  
RUN sudo pacman --noconfirm -S pulseaudio  
RUN sudo pacman --noconfirm -S alsa-utils  
# RUN yaourt --noconfirm -S spotify  
  
# add tung to audio group so you can run `alsamixer` later to unmute  
RUN sudo usermod -aG audio tung  
  
USER tung  
  

