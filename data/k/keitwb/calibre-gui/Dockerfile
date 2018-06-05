FROM keitwb/calibre-base:2.59  
MAINTAINER Ben Keith <keitwb@gmail.com>  
  
EXPOSE 5900  
ENTRYPOINT ["/entrypoint"]  
ENV DISPLAY :1  
RUN apt-get update -qq &&\  
apt-get install -y -qq \  
x11vnc \  
supervisor \  
fluxbox \  
xserver-xorg-video-dummy-lts-trusty \  
evince \  
firefox \  
inotify-tools \  
&&\  
apt-get clean  
  
COPY supervisor.conf /opt/calibre/supervisord.conf  
COPY xorg.conf /etc/X11/xorg.conf  
COPY scripts /scripts  
COPY entrypoint /entrypoint  
  

