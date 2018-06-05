FROM ubuntu:xenial  
  
RUN apt-get update -y  
RUN apt-get install -y xvfb  
RUN apt-get install -y x11vnc  
RUN apt-get install -y fluxbox  
RUN apt-get install -y arandr  
RUN apt-get install -y lxrandr  
  
# set up entrypoint script  
ADD init /init  
RUN chmod a+x,a-w /init  
  
# set up addresolution helper script  
ADD addresolution /usr/local/bin/addresolution  
RUN chmod a+x,a-w /usr/local/bin/addresolution  
  
# set up fluxbox menu  
RUN mkdir -p /root/.fluxbox  
ADD fluxbox_menu /root/.fluxbox/menu  
  
# set display environment variable  
ENV DISPLAY :0  
ENTRYPOINT ["/init"]  

