FROM node:7.5.0-alpine  
  
MAINTAINER UPX Technologies "labs@upx.com"  
RUN apk update \  
&& apk add \  
git \  
vim \  
curl \  
wget \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g \  
spectacle-docs  
  
ADD ./logo.png /root/logo.png  
  
WORKDIR /root  
  
CMD spectacle -d api-spec.yml -p 80 -l logo.png  

