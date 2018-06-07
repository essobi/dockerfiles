FROM node:9-alpine  
  
RUN apk --update add \  
sudo \  
openssl \  
bash \  
openssh \  
curl \  
wget \  
git \  
nano  
  
# added chromium  
# chromeOptions: {  
# args: [  
# '--no-sandbox',  
# '--headless',  
# '--disable-gpu',  
# '--disable-translate',  
# '--disable-extensions'  
# ],  
# binary: '/usr/bin/chromium-browser'  
# }  
# Update apk repositories  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" >
/etc/apk/repositories  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# selenium  
RUN apk --update add openjdk8-jre  
  
# Install chromium  
RUN apk -U --no-cache \  
\--allow-untrusted add \  
zlib-dev \  
chromium \  
chromium-chromedriver \  
xvfb \  
wait4ports \  
xorg-server \  
dbus \  
ttf-freefont \  
mesa-dri-swrast \  
grep \  
udev \  
&& apk del --purge --force linux-headers binutils-gold gnupg zlib-dev libc-
utils \  
&& rm -rf /var/lib/apt/lists/* \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/lib/node_modules/npm/scripts  
  
ENV CHROME_BIN=/usr/bin/chromium-browser  
ENV CHROME_PATH=/usr/lib/chromium/  
  
CMD [ "node" ]

