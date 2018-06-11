FROM yellowblackandwhite/alpine-selenium  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
#============================  
# Some configuration options  
#============================  
ENV SCREEN_WIDTH 1360  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
ENV VNC_PORT 5900  
ENV NODE_PORT 5555  
ENV NODE_MAX_INSTANCES 1  
ENV SELENIUM_BROWSER_NAME '*googlechrome'  
ENV WEBDRIVER_BROWSER_NAME 'chrome'  
#=====  
# VNC, fluxbox, Fonts, Chromium  
#=====  
USER root  
RUN apk add --update alpine-base sudo xvfb libx11 randrproto xineramaproto
lxdm libc6-compat fluxbox \  
font-misc-misc font-dec-misc font-cronyx-cyrillic font-misc-cyrillic font-
screen-cyrillic font-winitzki-cyrillic \  
font-bh-lucidatypewriter-100dpi font-bh-lucidatypewriter-75dpi xf86-video-
fbdev \  
xf86-video-dummy xf86-input-synaptics xf86-input-evdev && \  
apk add --update x11vnc --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \  
apk add --update chromium chromium-chromedriver --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ --allow-untrusted && \  
rm -rf /var/cache/apk/*  
#=======  
# Flash  
#=======  
ADD
https://fpdownload.macromedia.com/get/flashplayer/current/licensing/linux/install_flash_player_11_linux.x86_64.tar.gz
/tmp/  
RUN mkdir /tmp/install_flash_player_11_linux && \  
mkdir /usr/lib/flash-plugin/ && \  
mkdir -p /usr/lib/flash-plugin/ && \  
mkdir -p /usr/lib/firefox/browser/plugins/ && \  
tar -zxvf /tmp/install_flash_player_11_linux.x86_64.tar.gz -C
/tmp/install_flash_player_11_linux && \  
cd /tmp/install_flash_player_11_linux && \  
cp -r usr/* /usr && \  
cp libflashplayer.so /usr/lib/flash-plugin/ && \  
cp libflashplayer.so /usr/lib/firefox/browser/plugins/ && \  
chmod 775 /usr/lib/flash-plugin/libflashplayer.so && \  
chmod 775 /usr/lib/firefox/browser/plugins/libflashplayer.so && \  
rm -rf /tmp/install_flash_player_11_linux  
#==============================  
# Scripts to run Selenium Node  
#==============================  
ADD entry_point.sh ${SELENIUM_DIR}/entry_point.sh  
ADD generate_config ${SELENIUM_DIR}/generate_config  
RUN rc-update add lxdm default && \  
rc-update add acpid default && \  
mkdir /tmp/.X11-unix && \  
chmod -R a+rwx /tmp && \  
chmod 1777 /tmp/.X11-unix && \  
chmod +x ${SELENIUM_DIR}/entry_point.sh && \  
chmod +x ${SELENIUM_DIR}/generate_config && \  
chown -R seluser /opt/selenium  
  
USER seluser  
RUN mkdir -p ~/.vnc && x11vnc -storepasswd secret ~/.vnc/passwd  
  
EXPOSE ${VNC_PORT}  
CMD ["./entry_point.sh"]  

