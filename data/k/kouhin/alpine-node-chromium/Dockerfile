FROM node:8.9.4-alpine  
  
ENV CHROME_BIN /usr/bin/chromium-browser  
ENV LIGHTHOUSE_CHROMIUM_PATH /usr/bin/chromium-browser  
  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add --update --no-cache \  
bash \  
git \  
curl \  
chromium@community \  
harfbuzz@edge \  
freetype@edge \  
ttf-freefont \  
build-base \  
libpng-dev \  
zlib-dev \  
autoconf \  
automake \  
nasm \  
python \  
ca-certificates \  
wget && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk  

