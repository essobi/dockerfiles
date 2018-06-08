FROM jess/firefox  
  
RUN apt-get update && apt-get -y install pulseaudio  
  
RUN echo "deb http://deb.debian.org/debian sid contrib non-free"
>>/etc/apt/sources.list  
RUN apt-get update && apt-get install -y ttf-mscorefonts-installer  

