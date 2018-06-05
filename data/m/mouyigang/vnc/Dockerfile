FROM mouyigang/firefox  
MAINTAINER Andy <andy@edirect.asia>  
  
# Install LXDE, VNC server and Firefox  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
lxde-core \  
lxterminal \  
tightvncserver  
# Set user for VNC server (USER is only for build)  
ENV USER root  
# Set default password  
COPY password.txt .  
RUN cat password.txt password.txt | vncpasswd && \  
rm password.txt  
# Expose VNC port  
EXPOSE 5901  
# Copy VNC script that handles restarts  
COPY vnc.sh /opt/  
RUN chmod +x /opt/vnc.sh  
CMD ["/opt/vnc.sh"]  

