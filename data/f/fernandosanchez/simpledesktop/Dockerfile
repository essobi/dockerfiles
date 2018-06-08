FROM ubuntu:trusty  
MAINTAINER Sean Payne <seantpayne+docker@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD startup.sh /startup.sh  
  
RUN apt-get update -y && \  
apt-get install -y git x11vnc wget python python-numpy unzip Xvfb firefox
xfce4 xfce4-goodies geany menu \  
gconf-service libnspr4 libnss3 fonts-liberation \  
libappindicator1 libcurl3 fonts-wqy-microhei libglu1-mesa && \  
apt-get install -f && \  
cd /root && git clone https://github.com/fernandosanchezmunoz/noVNC.git && \  
cd noVNC/utils && git clone https://github.com/fernandosanchezmunoz/websockify
websockify && \  
cd /root && \  
chmod 0755 /startup.sh && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
COPY xfce4 ./.config/xfce4  
  
EXPOSE 5902 80 6080  
CMD /startup.sh  
  

