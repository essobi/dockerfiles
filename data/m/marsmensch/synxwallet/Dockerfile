#  
# Dockerfile to run Syndicate-QT Wallet and access it through the browser  
# https://bitcointalk.org/index.php?topic=1511215.0  
# _____ _ _ _  
# | __|_ _ ___ _| |_|___ ___| |_ ___  
# |__ | | | | . | | _| .'| _| -_|  
# |_____|_ |_|_|___|_|___|__,|_| |___|  
# |___|  
#  
# tip me at:  
# BTC 1PboFDkBsW2i968UnehWwcSrM9Djq5LcLB  
# SYNX SSKYwMhQQt9DcWozt7zA1tR3DmRuw1gT6b  
#  
# BUILD: docker build -t marsmensch/synxwallet:latest .  
# RUN: docker run -it -p 6080:6080 marsmensch/synxwallet  
# TEST: docker run --interactive --tty --entrypoint=/bin/bash
marsmensch/synxwallet  
#  
FROM marsmensch/synx  
MAINTAINER Florian Maier <contact@marsmenschen.com>  
ENV REFRESHED_AT 2016-07-11  
# Set environment variables (can be changed on docker run with -e)  
ENV NOVNC_GIT_URL git://github.com/kanaka/noVNC.git  
ENV WBSKY_GIT_URL git://github.com/kanaka/websockify  
ENV NOVNC_BASEDIR /opt/noVNC  
ENV DISPLAY :1  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean && \  
apt-get autoremove && apt-get update && \  
apt-get -qqy install --no-install-recommends \  
git x11vnc fluxbox firefox eterm x11-utils wget python python-numpy unzip xvfb
curl tar bzip2 net-tools runit  
  
# NoVNC code directory  
RUN cd /opt; git clone ${NOVNC_GIT_URL} noVNC && \  
cd ${NOVNC_BASEDIR}/utils && git clone ${WBSKY_GIT_URL} websockify && \  
cd ${NOVNC_BASEDIR} && ln -s auto_vnc.html index.html  
  
# Runit config  
RUN bash -c "mkdir -p /etc/service/{X11vnc,noVNC,synx}"  
ADD startup/X11vnc.run /etc/service/X11vnc/run  
ADD startup/noVNC.run /etc/service/noVNC/run  
ADD startup/fluxbox.run /etc/service/fluxbox/run  
ADD startup/synx.run /etc/service/synx/run  
ADD synx.png /opt/synx.png  
  
RUN chmod -R +x /etc/service  
  
EXPOSE 6080  
CMD [ "/usr/bin/runsvdir", "-P", "/etc/service" ]  

