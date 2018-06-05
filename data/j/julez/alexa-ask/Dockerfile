FROM node:6.12.3-alpine  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& pip install boto \  
&& npm -g install ask-cli \  
&& rm -rf /var/cache/apk/*  
  

