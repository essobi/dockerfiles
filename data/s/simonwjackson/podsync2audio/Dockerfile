FROM node:7.7.2-alpine  
  
RUN apk update && apk add --no-cache bash  
  
RUN set -x \  
&& apk add --no-cache ca-certificates curl ffmpeg python \  
# Install youtube-dl  
# https://github.com/rg3/youtube-dl  
&& curl -Lo /usr/local/bin/youtube-dl https://yt-
dl.org/downloads/latest/youtube-dl \  
&& chmod a+rx /usr/local/bin/youtube-dl \  
# Clean-up  
&& apk del curl \  
&& youtube-dl --version  
  
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt  
  
COPY package.json /tmp/package.json  
RUN cd /tmp && npm install --quiet  
RUN mkdir -p /usr/app && cp -a /tmp/node_modules /usr/app  
  
COPY ./ /usr/app/  
  
# HACK: ensure the linux version gets used  
RUN rm -f /usr/app/node_modules/youtube-dl/bin/youtube-dl.exe \  
&& ln -s /usr/app/node_modules/youtube-dl/bin/youtube-dl
/usr/app/node_modules/youtube-dl/bin/youtube-dl.exe \  
&& /usr/app/node_modules/youtube-dl/bin/youtube-dl.exe \--version  
  
WORKDIR /usr/app  
  
EXPOSE 8080  
  
CMD [ "npm", "run", "dev" ]  

