FROM ruby:2.2-alpine  
  
RUN apk -U --no-cache upgrade \  
\--repository http://dl-cdn.alpinelinux.org/alpine/v3.6/main \  
\--repository http://dl-cdn.alpinelinux.org/alpine/v3.6/community  
  
RUN apk -U --no-cache add \  
nodejs \  
curl \  
wget \  
git \  
python \  
make \  
gcc \  
libxtst-dev \  
libpng-dev \  
g++ \  
openjdk8 \  
xvfb \  
chromium \  
chromium-chromedriver \  
dbus \  
ttf-freefont \  
udev \  
\--repository http://dl-cdn.alpinelinux.org/alpine/v3.6/main \  
\--repository http://dl-cdn.alpinelinux.org/alpine/v3.6/community  

