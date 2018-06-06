FROM codeworksio/ubuntu:18.04-20180210  
  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV VNC_DISPLAY=":1" \  
VNC_RESOLUTION="1280x1024" \  
VNC_COLOUR_DEPTH="24" \  
VNC_PASSWORD="ubuntu"  
  
RUN set -ex; \  
\  
# install system packages  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
apt-get --yes update; \  
apt-get --yes upgrade; \  
apt-get --yes install \  
dbus-x11 \  
tightvncserver \  
xbase-clients \  
xfce4 \  
xfce4-terminal \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-base \  
xfonts-scalable \  
; \  
# configure system user  
echo "root:$VNC_PASSWORD" | chpasswd; \  
mkdir -p /home/$SYSTEM_USER/.vnc; \  
touch /home/$SYSTEM_USER/.Xresources; \  
touch /home/$SYSTEM_USER/.Xauthority; \  
\  
# SEE: https://github.com/stefaniuk/dotfiles  
curl -L https://raw.githubusercontent.com/stefaniuk/dotfiles/master/dotfiles
-o - | /bin/bash -s -- \  
\--directory=/home/$SYSTEM_USER \  
\--minimal; \  
chown -R $SYSTEM_USER:$SYSTEM_USER /home/$SYSTEM_USER; \  
chsh -s /bin/bash $SYSTEM_USER; \  
\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
COPY assets/ /  
  
WORKDIR /home/$SYSTEM_USER  
EXPOSE 5901-5999  
CMD [ "/sbin/init.sh" ]  
  
### METADATA
###################################################################  
  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

