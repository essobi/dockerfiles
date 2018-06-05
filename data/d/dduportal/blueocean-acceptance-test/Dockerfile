FROM maven:3.3-jdk-8  
MAINTAINER Damien Duportal <dduportal@cloudbees.com>  
  
## Common Part  
ENV DEBIAN_FRONTEND=noninteractive \  
LC_ALL=C.UTF-8 \  
USER=dev \  
FIREFOX_VERSION=44.0.2 \  
DISPLAY=:0 \  
VNC_COL_DEPTH=24 \  
VNC_RESOLUTION=1280x800 \  
VNC_PW=vncpass \  
BROWSER=firefox \  
TERM=ansi \  
NOVNC_ARGS="--listen 9000 --vnc localhost:5900"  
# Installing the X Server and GUI Desktop  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
fontconfig \  
gnome-icon-theme \  
libxml2-utils \  
localepurge \  
net-tools \  
nodejs \  
scite \  
sudo \  
ssh-client \  
tango-icon-theme \  
vim \  
vnc4server \  
xfce4 \  
xfce4-terminal \  
xfonts-base \  
xvfb \  
&& apt-get autoremove --purge -y \  
&& apt-get clean -y \  
&& localepurge \  
&& rm -rf \  
/var/log/* \  
/tmp/* \  
/var/lib/apt/lists/* \  
/usr/share/doc/*  
  
# Installing Firefox from official binaries dist for x86_64  
RUN curl -L -o /tmp/firefox.tar.bz2 \  
"http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/en-
US/firefox-${FIREFOX_VERSION}.tar.bz2" \  
&& tar jxf /tmp/firefox.tar.bz2 -C /opt/ \  
&& ln -s /opt/firefox/firefox /usr/local/bin/  
  
# Installing noVNC  
ENV NOVNC_DIR=/opt/noVNC  
RUN git clone https://github.com/kanaka/noVNC.git "${NOVNC_DIR}" \  
&& git clone https://github.com/kanaka/websockify
"${NOVNC_DIR}/utils/websockify" \  
&& rm -rf "${NOVNC_DIR}/.git" \  
&& rm -rf "${NOVNC_DIR}/utils/websockify/.git"  
  
# Creating user  
RUN useradd --home-dir /home/${USER} \--create-home --shell /bin/bash --user-
group ${USER} \  
&& echo "${USER}:${USER}" | chpasswd \  
&& adduser ${USER} sudo  
  
# Get Blueocean code  
RUN git clone https://github.com/jenkinsci/blueocean-plugin
/home/${USER}/blueocean-plugin  
RUN git clone https://github.com/jenkinsci/blueocean-acceptance-test
/home/${USER}/blueocean-acceptance-test  
  
# Copying config for GUi and Firefox  
COPY ./xstartup "/home/${USER}/.vnc/xstartup"  
COPY ./xfce4-config "/home/${USER}/.config/xfce4"  
COPY ./build-blueocean.sh "/home/${USER}/build-blueocean.sh"  
COPY ./firefox-configs/mozilla.cfg /opt/firefox/  
COPY ./firefox-configs/local-settings.js /opt/firefox/defaults/pref/  
  
RUN chown -R $USER:$USER "/home/${USER}" \  
&& chmod 0755 "/home/${USER}/.vnc/xstartup" "${NOVNC_DIR}/utils/launch.sh"
"/home/${USER}/build-blueocean.sh" \  
&& chmod 0644 /opt/firefox/mozilla.cfg /opt/firefox/defaults/pref/* \  
&& su ${USER} sh -c "(echo ${VNC_PW} && echo ${VNC_PW}) | vncpasswd"  
  
EXPOSE 5900 9000  
USER dev  
WORKDIR /home/${USER}  
  
VOLUME ["/home/${USER}/.m2","/home/${USER}/blueocean-acceptance-
test","/home/${USER}/blueocean-plugin"]  
  
ENTRYPOINT vncserver ${DISPLAY} -depth ${VNC_COL_DEPTH} \  
-geometry ${VNC_RESOLUTION} -fp /usr/share/fonts/X11/misc \  
&& tail -f /home/${USER}/.vnc/*${DISPLAY}.log  

