FROM yellowblackandwhite/alpine-jre  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
  
ENV SELENIUM_DIR /opt/selenium/  
ENV SELENIUM_BIN ${SELENIUM_DIR}/selenium-server-standalone.jar  
ENV SELENIUM_VER 2.53  
ENV SELENIUM_VER_FULL 2.53.0  
ENV SELENIUM_PORT 4444  
ENV GRID_NEW_SESSION_WAIT_TIMEOUT -1  
ENV GRID_JETTY_MAX_THREADS -1  
ENV GRID_NODE_POLLING 5000  
ENV GRID_CLEAN_UP_CYCLE 5000  
ENV GRID_TIMEOUT 30000  
ENV GRID_BROWSER_TIMEOUT 0  
ENV GRID_MAX_SESSION 5  
ENV GRID_UNREGISTER_IF_STILL_DOWN_AFTER 30000  
ADD http://selenium-release.storage.googleapis.com/${SELENIUM_VER}/selenium-
server-standalone-${SELENIUM_VER_FULL}.jar ${SELENIUM_BIN}  
ADD entry_point.sh ${SELENIUM_DIR}/entry_point.sh  
ADD generate_config ${SELENIUM_DIR}/generate_config  
ADD xvfb-run /usr/bin/  
  
RUN apk add --update alpine-base bash sudo file xvfb sudo libx11 randrproto
xineramaproto lxdm libc6-compat fluxbox ircii \  
xf86-video-fbdev xf86-video-dummy xf86-input-synaptics xf86-input-evdev && \  
adduser -D seluser && echo 'seluser ALL=(ALL) ALL'>/etc/sudoers && \  
# mv /usr/lib/libX11.so.6 /usr/lib/libX11.so.6.bak && \  
# ln -s /usr/lib/libX11.so.6.3.0 /usr/lib/libX11.so.6 && \  
chmod a+x ${SELENIUM_DIR}/entry_point.sh && \  
chmod a+x ${SELENIUM_DIR}/generate_config && \  
chmod a+x /usr/bin/xvfb-run && \  
chown -R seluser ${SELENIUM_DIR} && \  
rm -rf /var/cache/apk/* && \  
mkdir -p ${SELENIUM_DIR}  
WORKDIR ${SELENIUM_DIR}  
  
USER seluser  
EXPOSE ${SELENIUM_PORT}  
ENTRYPOINT ["./entry_point.sh"]  

