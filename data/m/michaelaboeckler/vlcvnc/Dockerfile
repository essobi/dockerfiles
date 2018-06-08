FROM ubuntu:14.04  
MAINTAINER Michaela Böckler  
  
# Install LXDE, VNC server and VLC as root  
ENV USER root  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
vlc \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
lxde-core \  
lxterminal \  
tightvncserver  
  
# Expose VNC port  
EXPOSE 5901  
#set password for vnc  
RUN echo "vncpassword\nvncpassword\n\n" | vncpasswd  
  
COPY vncserver.sh /opt/  
COPY Wildlife.wmv /opt/  
RUN chmod +x /opt/vncserver.sh  
ENTRYPOINT ["/opt/vncserver.sh"]

