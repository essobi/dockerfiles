FROM patricol/ubuntu_vnc:Cuda  
  
USER root  
  
RUN apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
x11vnc xvfb net-tools \  
xserver-xorg-video-dummy && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
#Fix ubuntu weirdness with xorg https://xpra.org/trac/wiki/Xdummy  
RUN adduser user tty && \  
adduser user video && \  
adduser user dialout  
  
EXPOSE 6080 5901  
RUN git clone https://github.com/novnc/noVNC.git /opt/noVNC && \  
git clone https://github.com/kanaka/websockify /opt/noVNC/utils/websockify  
  
#COPY --chown=root:root extras/index.html /opt/noVNC/#Not yet supported by
docker hub's automated builds, which use an outdated version of docker.  
COPY extras/index.html /opt/noVNC/  
#COPY --chown=root:root extras/xorg.conf /etc/X11/#Not yet supported by docker
hub's automated builds, which use an outdated version of docker.  
COPY extras/xorg.conf /etc/X11/  
#COPY --chown=root:root extras/novnc.conf /etc/supervisor/conf.d/#Not yet
supported by docker hub's automated builds, which use an outdated version of
docker.  
COPY extras/novnc.conf /etc/supervisor/conf.d/  
RUN echo '#!/bin/bash\ncat /home/user/password.txt\nsupervisorctl start
novnc:*' > /home/user/novnc.sh && \  
chmod +x /home/user/novnc.sh  
#Connection startup considerations:  
#Running novnc stuff immediately at startup often breaks because it can
execute before the password-setting stuff is finished.  
#Adding it to earlycommands.sh makes it hard to toggle with ENV variables.
(root executes that script, ignoring env variables set by ENV in dockerfiles.)  
#Most importantly, when run on low-powered machines, starting all connection
methods automatically every time is bad for performance.  
#That's why I'm putting this in a startup script.  
USER user

