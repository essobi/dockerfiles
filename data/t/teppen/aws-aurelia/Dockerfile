FROM node:alpine  
LABEL maintainer "tom@teppen.io"  
RUN apk -v --update add \  
python \  
py-pip \  
git \  
&& \  
pip install --upgrade awscli && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  

