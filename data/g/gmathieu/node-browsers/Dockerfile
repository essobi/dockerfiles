# https://store.docker.com/images/node  
FROM node:8-stretch  
  
# https://packages.debian.org/stretch/chromium  
# https://packages.debian.org/stretch/firefox-esr  
ARG CHROMIUM=66.0.3359.117-1~deb9u1  
ARG FIREFOX=52.8.0esr-1~deb9u1  
  
RUN \  
apt-get update && apt-get install -y \  
# browsers  
chromium=${CHROMIUM} firefox-esr=${FIREFOX} \  
# GUI: Firefox ESR 52 has no -headless  
dbus xvfb \  
# cci deps  
git tar gzip ca-certificates \  
# deployment  
bash curl make \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
# GUI  
ADD bin/xvfb-firefox /usr/bin/xvfb-firefox  
  
ENV \  
# disable puppeteer download as it will not work with this image  
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \  
# browser bin paths  
CHROME_BIN=/usr/bin/chromium \  
FIREFOX_BIN=/usr/bin/xvfb-firefox  

