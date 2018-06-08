FROM alpine:3.5  
MAINTAINER Joe Brutto  
  
ENV APK_SIGNATURE -58b7ee0c  
ENV OSSP_UUID_VERSION 1.6.2-r0  
ENV X11VNC_VERSION 0.9.13-r0  
  
# install ossp-uuid  
ADD /apk /apk  
RUN \  
cp /apk/${APK_SIGNATURE}.rsa.pub /etc/apk/keys && \  
apk --update add /apk/ossp-uuid-${OSSP_UUID_VERSION}.apk && \  
apk add /apk/ossp-uuid-dev-${OSSP_UUID_VERSION}.apk  
  
# install VNC & the desktop system  
RUN \  
apk add /apk/x11vnc-${X11VNC_VERSION}.apk && \  
apk add xvfb xfce4 xfce4-terminal openbox faenza-icon-theme  
  
# set up support for supervisord & our core users  
RUN \  
apk add supervisor sudo && \  
addgroup alpine && \  
adduser -G alpine -s /bin/sh -D alpine && \  
echo "alpine:alpine" | /usr/sbin/chpasswd && \  
echo "alpine ALL=(ALL) ALL" >> /etc/sudoers && \  
mkdir -p /etc/supervisor/conf.d  
  
# clean-up  
RUN \  
rm -Rf /apk /tmp/* /var/cache/apk/*  
  
# service configuration  
ADD /services/supervisord.conf /etc/supervisord.conf  
ADD /services/conf.d/* /etc/supervisor/conf.d/  
  
# start the system  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

