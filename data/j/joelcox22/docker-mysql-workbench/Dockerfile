FROM ubuntu:16.04  
  
RUN \  
apt-get update -y && \  
apt-get install --no-install-recommends -y \  
x11vnc xvfb xterm lxde mysql-workbench  
  
EXPOSE 5900  
VOLUME /config  
  
ENV DISPLAY=:0 SCREEN_WIDTH=1024 SCREEN_HEIGHT=768 HOME=/config  
  
ADD start.sh /start.sh  
CMD ["/start.sh"]  
  

