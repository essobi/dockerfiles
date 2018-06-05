FROM ubuntu:16.04  
# Install LXDE, VNC server, XRDP and Firefox  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
firefox lxde-core lxterminal tightvncserver xrdp  
  
# Set user for VNC server (USER is only for build)  
ENV USER root  
# Set default password  
COPY password.txt .  
RUN cat password.txt password.txt | vncpasswd && \  
rm password.txt  
# Expose VNC port  
EXPOSE 5901  
# Set XDRP to use TightVNC port  
RUN sed -i '0,/port=-1/{s/port=-1/port=5901/}' /etc/xrdp/xrdp.ini  
  
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  
  
# Copy VNC script that handles restarts  
COPY vnc.sh /opt/  
RUN chmod +x /opt/vnc.sh  
CMD ["/opt/vnc.sh"]  

