FROM ubuntu:xenial  
MAINTAINER Matthias Berla  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SDL_AUDIODRIVER=alsa  
ENV HOME /home/steam  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get install -yq wget curl zenity libgl1-mesa-
dri:i386 libgl1-mesa-glx:i386 libc6:i386 sudo python-apt xterm  
RUN wget http://media.steampowered.com/client/installer/steam.deb  
RUN sudo dpkg -i steam.deb && sudo apt-get install -f && sudo dpkg -i
steam.deb  
RUN echo 'steam ALL = NOPASSWD: ALL' > /etc/sudoers.d/steam && chmod 0440
/etc/sudoers.d/steam  
  
RUN adduser --disabled-password --gecos 'Steam' steam && adduser steam video  
USER steam  
VOLUME /home/steam  
  
CMD ["steam"]  

