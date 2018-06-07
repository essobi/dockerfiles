#  
# Dockerfile run Gambit and access it through the browser  
#  
# BUILD: docker build -t marsmensch/gambitweb:latest .  
# RUN: docker run -it -p 6080:6080 marsmensch/gambitweb  
# TEST: docker run --interactive --tty --entrypoint=/bin/bash
marsmensch/gambitweb  
#  
FROM marsmensch/gambitcrypto  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
ENV REFRESHED_AT 2016-05-16  
# Set environment variables (can be changed on docker run with -e)  
ENV NOVNC_GIT_URL git://github.com/kanaka/noVNC.git  
ENV WBSKY_GIT_URL git://github.com/kanaka/websockify  
ENV NOVNC_BASEDIR /opt/noVNC  
ENV DISPLAY :1  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean && \  
apt-get autoremove && apt-get update && \  
apt-get -qqy install --no-install-recommends \  
git x11vnc fluxbox eterm x11-utils wget python python-numpy unzip xvfb curl
tar bzip2 net-tools runit  
  
# NoVNC code directory  
RUN cd /opt; git clone ${NOVNC_GIT_URL} noVNC && \  
cd ${NOVNC_BASEDIR}/utils && git clone ${WBSKY_GIT_URL} websockify && \  
cd ${NOVNC_BASEDIR} && ln -s auto_vnc.html index.html  
  
# Runit config  
RUN bash -c "mkdir -p /etc/service/{X11vnc,noVNC,gambit}"  
ADD startup/X11vnc.run /etc/service/X11vnc/run  
ADD startup/noVNC.run /etc/service/noVNC/run  
ADD startup/fluxbox.run /etc/service/fluxbox/run  
ADD startup/gambit.run /etc/service/gambit/run  
ADD gambit.jpeg /opt/gambit.jpeg  
  
RUN chmod -R +x /etc/service  
  
EXPOSE 6080  
CMD [ "/usr/bin/runsvdir", "-P", "/etc/service" ]  

