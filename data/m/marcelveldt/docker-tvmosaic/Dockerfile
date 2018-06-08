FROM debian:stretch  
LABEL maintainer="Marcel van der Veldt <m.vanderveldt@outlook.com>"  
  
ENV LANG C.UTF-8  
VOLUME /config  
VOLUME /recordings  
EXPOSE 9270 9271  
RUN apt-get update && \  
apt-get install -y wget dbus gconf2 && \  
wget -nv http://tv-mosaic.com/download/624e68fb8cfab4ce8d277d4a416af741 -O
tvmosaic.deb && \  
dpkg -i tvmosaic.deb  
  
CMD [ "/usr/local/bin/tvmosaic/start.sh" ]  

