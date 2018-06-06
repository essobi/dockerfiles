# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-base:debian  
MAINTAINER t.dettrick@uq.edu.au  
  
# Install  
# - MESA DRI drivers for software GLX rendering  
# - X11 dummy & void drivers  
# - RandR utility  
# - X11 xinit binary  
# - reasonable fonts for UI  
# - x11vnc  
# - python-websockify  
# - openbox  
# - tint2  
# - xterm  
# - lxrandr  
# - nitrogen  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libgl1-mesa-dri \  
xserver-xorg-video-dummy \  
xserver-xorg-input-void \  
x11-xserver-utils \  
xinit \  
fonts-dejavu \  
x11vnc \  
websockify \  
openbox \  
tint2 \  
xterm \  
lxrandr \  
nitrogen && \  
rm -f /usr/share/applications/x11vnc.desktop && \  
apt-get clean  
  
# Get modified build of noVNC  
RUN git clone -b override-touch https://github.com/dit4c/noVNC.git /opt/noVNC
&& \  
rm -rf /opt/noVNC/.git  
  
# Add supporting files (directory at a time to improve build speed)  
COPY etc /etc  
COPY usr /usr  
COPY var /var  
  
RUN echo "allowed_users=anybody" > /etc/X11/Xwrapper.config  
  
# Check nginx config is OK  
RUN nginx -t  

