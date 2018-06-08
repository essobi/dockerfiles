FROM node:alpine  
  
MAINTAINER UPX Technologies "labs@upx.com"  
  
RUN apk update \  
&& apk add \  
git \  
vim \  
curl \  
wget \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g --quiet \  
sass-lint  

