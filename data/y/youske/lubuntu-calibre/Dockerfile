# Lubuntu Linux with calibre  
# ubuntu:16.04  
FROM youske/ubuntu-stdmachine:base  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="lubuntu calibre ebook management image" \  
com.stdmachine.role="calibre" \  
com.stdmachine.os="ubuntu"  
  
#----- common -----  
ENV COMMONPACKAGE='bash vim-tiny logrotate supervisor git tig tmux bzip2 curl
wget ca-certificates' \  
LUBUNTUPACKAGE='xorg xterm lxde-core lxappearance lxsession-data lxterminal
lxinput lubuntu-icon-theme lubuntu-artwork-16-04 lubuntu-lxpanel-icons
lubuntu-artwork xfonts-100dpi xfonts-100dpi-transcoded xfonts-75dpi
xfonts-75dpi-transcoded xfonts-base ' \  
FONTPACKAGE='fonts-ipafont-mincho fonts-ipafont-gothic' \  
LANGPACKAGE='locales language-pack-ja language-pack-ja ibus-mozc'  
# apt-get install  
RUN apt-get update && apt-get -y -q upgrade && \  
DEBIAN_FRONTEND=nointeractive apt-get install -y ${COMMONPACKAGE}
${LUBUNTUPACKAGE} ${FONTPACKAGE} ${LANGPACKAGE} && \  
update-locale LANG=${LANGUAGE:-ja_JP.UTF-8}  
  
#------ calibre ------  
ENV CALIBRE_USER='calibre' \  
CALIBRE_PASSWORD='calibreadmin' \  
CALIBRE_MAXCOVER="300x280" \  
CALIBRE_PORT=8088 \  
CALIBRE_LIBRARY="/Calibre_Library" \  
CALIBRE_URL=https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py \  
CALIBRE_PACKAGE='imagemagick okular python-pip python-dev build-essential'  
# calibre install  
RUN DEBIAN_FRONTEND=nointeractive apt-get install -y -q ${CALIBRE_PACKAGE}  
# && \  
RUN wget -q --no-check-certificate ${CALIBRE_URL} -O- | python -c "import sys;
main=lambda:sys.stderr.write('Download Failed\n'); exec(sys.stdin.read());
main()"  
RUN mkdir -p "${CALIBRE_LIBRARY}" && mkdir -p "${CALIBRE_LIBRARY}/import" && \  
chown -R ${VNC_USER}:${VNC_USER} "${CALIBRE_LIBRARY}"  
  
#----- vnc -----  
ENV VNC_USER="${VNC_USER:-vnc}" \  
VNC_PASSWORD="${VNC_PASSWORD:-vncpass}" \  
VNC_PORT="${VNC_PORT:-5901}" \  
VNC_DEPTH="${VNC_DEPTH:-24}" \  
VNC_DISPLAY="${VNC_DISPLAY:-1}" \  
VNC_GEOMETRY="${VNC_GEOMETRY:-1280x800}"  
ENV VNC_HOME="/home/${VNC_USER}"  
COPY install_vnc /tmp/install_vnc  
RUN . /tmp/install_vnc  
COPY start.sh ${VNC_HOME}/start.sh  
RUN chmod +x ${VNC_HOME}/start.sh && chown -R ${VNC_USER}:${VNC_USER}
${VNC_HOME}  
  
#  
COPY xstartup ${VNC_HOME}/.vnc/  
RUN chmod +x ${VNC_HOME}/.vnc/xstartup  
  
# remove build package  
RUN apt-get autoremove -y python-dev build-essential && rm -rf /tmp/*
/var/cache/apk/*  
  
EXPOSE ${CALIBRE_PORT} ${VNC_PORT}  
WORKDIR ${VNC_HOME}  
ENTRYPOINT ["switch","shell=/bin/bash","--","/init"]  
CMD
["gosu","vnc","vncserver",":${VNC_DISPLAY}","-fg","-geometry","${VNC_GEOMETRY}","-depth","${VNC_DEPTH}"]  

