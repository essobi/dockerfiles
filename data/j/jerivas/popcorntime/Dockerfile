# Base docker image  
# docker run -ti --rm jerivas/popcorntime /config > popcorntime.sh  
# chmod +x popcorntime.sh  
# dos2unix popcorntime.sh  
# ./popcorntime.sh  
# ```  
#  
# The next time do:  
#  
# ```  
# docker start popcorn  
# ```  
#  
# RUN popcorntime.sh  
FROM debian:stretch-slim  
MAINTAINER jerivas<jerivas@uaq.edu.mx>  
  
  
RUN \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \  
libgtk2.0-0:i386 libnss3 libgconf-2-4 libasound2-plugins libnotify4 \  
alsa-tools alsa-utils pulseaudio  
  
RUN \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
gconf-service \  
hicolor-icon-theme \  
libappindicator1 \  
libasound2 \  
libcanberra-gtk-module \  
libcurl3 \  
libexif-dev \  
libgconf-2-4 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libnspr4 \  
libnss3 \  
libpango1.0-0 \  
libv4l-0 \  
libxss1 \  
libxtst6 \  
wget \  
xdg-utils  
  
RUN \  
apt-get install -y --no-install-recommends xz-utils  
  
RUN \  
apt-get install -y --no-install-recommends libudev-dev libudev1  
  
#RUN wget -O popcorn-time.tar.xz
http://popcorntime.ag/download.php?file=popcorn-time-
community-v0.4.0-2-l64.tar.xz  
#RUN wget -O popcorn-time.tar.xz
http://popcorntimece.ch/Downloads/Popcorn%20Time%20CE%20x64%20Linux.tar.xz  
#RUN wget -O popcorn-time.tar.xz
https://popcorntime.sh/download/build/Popcorn-Time-0.3.9-Linux-64.tar.xz  
#RUN wget -O popcorn-time.tar.xz
https://popcorntime.sh/download/build/Popcorn-Time-0.3.9-Linux-64.tar.xz  
#RUN wget -O popcorn-time.tar.xz http://mirror02.popcorntime.sh/build/Popcorn-
Time-0.3.10-Linux-64.tar.xz  
#RUN wget -O popcorn-time.tar.xz http://mirror02.popcorntime.sh/build/Popcorn-
Time-0.3.10-Linux-64.tar.xz  
RUN wget -O popcorn-time.tar.xz http://mirror02.popcorntime.sh/build/Popcorn-
Time-0.3.10-Linux-64.tar.xz  
  
RUN mkdir /opt/popcorntime/ && tar xvf popcorn-time.tar.xz -C
/opt/popcorntime/  
  
RUN ln -sf /lib/$(arch)-linux-gnu/libudev.so.1 /lib/$(arch)-linux-
gnu/libudev.so.0  
  
# Remove temporary files  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY start.sh start-withNvidia.sh config.sh config-withNvidia.sh /  
  
ENTRYPOINT [ "/opt/popcorntime/Popcorn-Time" ]  
  

