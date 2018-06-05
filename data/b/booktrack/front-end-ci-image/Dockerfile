FROM node:8-alpine  
  
# Useful search engine for determining what apk package is needed for a given
file  
#
https://pkgs.alpinelinux.org/contents?file=make&path=&name=&branch=v3.4&repo=main  
RUN apk update && apk add --no-cache \  
bash \  
git \  
openssh \  
xvfb \  
dbus \  
ttf-freefont \  
udev  
  
RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community \  
chromium \  
chromium-chromedriver  
  
ENV DISPLAY :99  
ENV CHROME_BIN /usr/bin/chromium  
  
# Install azure-cli 2.0  
RUN apk update && apk add \  
gcc \  
libffi-dev \  
make \  
musl-dev \  
openssl-dev \  
py2-pip \  
python2 \  
python2-dev  
  
RUN pip install --user azure-cli  
ENV PATH="/root/.local/bin:${PATH}"  

