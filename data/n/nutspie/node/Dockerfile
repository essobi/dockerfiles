FROM node:8-slim  
  
LABEL maintainer="dev@nutspie.com"  
  
USER root  
  
#============================================  
# Add Envs  
#============================================  
#============================================  
# Add packages  
#============================================  
# from https://hub.docker.com/r/selenium/node-chrome/~/dockerfile/  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN npm --global install yarn  
  
#============================================  
# Cleanup  
#============================================  
  
RUN apt-get remove --purge -y \  
curl \  
make \  
g++ \  
python \  
gnupg  
  
RUN rm -rf /var/lib/apt/lists/* \  
/var/cache/apk/* \  
/usr/share/man \  
/tmp/* \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html \  
/usr/lib/node_modules/npm/scripts  
#============================================  
# Setup  
#============================================  
  
WORKDIR /data  
VOLUME /data  
  
RUN ln -s google-chrome /usr/bin/chrome  

