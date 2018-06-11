# Lubuntu Linux with calibre  
  
FROM youske/ubuntu-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="lubuntu calibre ebook management image" \  
com.stdmachine.role="novnc"  
  
ENV LUBUNTUPACKAGE='xvfb x11vnc xterm mozc-server lxde-core lxappearance
lxsession-data lxterminal lxinput lubuntu-icon-theme lubuntu-artwork-16-04
lubuntu-lxpanel-icons lubuntu-artwork' \  
FONTPACKAGE='fonts-ipafont-mincho fonts-ipafont-gothic xfonts-100dpi
xfonts-100dpi-transcoded xfonts-75dpi xfonts-75dpi-transcoded xfonts-base'  
  
ENV NOVNC_PORT=8080  
  
# apt-get install  
RUN DEBIAN_FRONTEND=nointeractive apt-get update && apt-get -y upgrade && \  
DEBIAN_FRONTEND=nointeractive apt-get install -y wget ca-certificates  
#${LUBUNTUPACKAGE} ${FONTPACKAGE}  
  
# Download and install noVNC.  
RUN NOVNC_URL="http://github.com/kanaka/noVNC/tarball/master" && \  
WEBSOCKIFY_URL="https://github.com/kanaka/websockify/tarball/master" && \  
mkdir -p /opt/noVNC/utils/websockify && \  
wget -qO- ${NOVNC_URL} | tar -zx --strip-components=1 -C /opt/noVNC && \  
wget -qO- ${WEBSOCKIFY_URL} | tar -zx --strip-components=1 -C
/opt/noVNC/utils/websockify && \  
ln -s /opt/noVNC/vnc.html /opt/noVNC/index.html  
  
  
# Installing apps and clean up.  
RUN PACKAGE="xvfb x11vnc supervisor wget ca-certificates net-tools python" &&
\  
apt-get update && apt-get -y install ${PACKAGE} && apt-get clean  
  
# Install some additins.  
RUN PACKAGE="fluxbox fonts-ipafont-gothic mozc-server chromium-browser" && \  
apt-get update && apt-get -y install ${PACKAGE} && apt-get clean  
  
  
#\------ calibre ------  
  
#ENV CALIBRE_USER='calibre' \  
# CALIBRE_PASSWORD='calibreadmin' \  
# CALIBRE_MAXCOVER="300x280" \  
# CALIBRE_PORT=8088 \  
# CALIBRE_LIBRARY="/Calibre_Library" \  
#
CALIBRE_URL=https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py \  
# CALIBRE_PACKAGE='imagemagick okular python-pip python-dev build-essential'  
  
# calibre install  
#RUN DEBIAN_FRONTEND=nointeractive apt-get install -y ${CALIBRE_PACKAGE} && \  
# wget -q --no-check-certificate ${CALIBRE_URL} -O- | python -c "import sys;
main=lambda:sys.stderr.write('Download Failed\n'); exec(sys.stdin.read());
main()"  
#RUN mkdir -p "${CALIBRE_LIBRARY}" && mkdir -p "${CALIBRE_LIBRARY}/import" &&
\  
# chown -R ${VNC_USER}:${VNC_USER} "${CALIBRE_LIBRARY}"  
  
#\----- vnc -----  
  
#ENV VNC_USER="${VNC_USER:-vnc}" \  
# VNC_PASSWORD="${VNC_PASSWORD:-vncpass}" \  
# VNC_PORT="${VNC_PORT:-5901}" \  
# VNC_DEPTH="${VNC_DEPTH:-24}" \  
# VNC_DISPLAY="${VNC_DISPLAY:-1}" \  
# VNC_GEOMETRY="${VNC_GEOMETRY:-1280x800}"  
  
#ENV VNC_HOME="/home/${VNC_USER}"  
  
#COPY install_vnc /tmp/install_vnc  
#RUN . /tmp/install_vnc  
#COPY start.sh ${VNC_HOME}/start.sh  
#RUN chmod +x ${VNC_HOME}/start.sh && chown -R ${VNC_USER}:${VNC_USER}
${VNC_HOME}  
  
#  
#COPY xstartup ${VNC_HOME}/.vnc/  
#RUN chmod +x ${VNC_HOME}/.vnc/xstartup  
  
# remove build package  
#RUN apt-get autoremove -y python-dev build-essential && rm -rf /tmp/*
/var/cache/apk/*  
  
EXPOSE ${NOVNC_PORT}  
#WORKDIR ${VNC_HOME}  
COPY novnc.conf /etc/supervisor/conf.d/novnc.conf  
CMD ["/usr/bin/supervisord"]  

