FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
RUN apk add -U python3 \  
&& ln -s /usr/bin/python3 /usr/bin/python \  
&& ln -s /usr/bin/pip3 /usr/bin/pip \  
&& pip install --upgrade pip \  
&& rm /var/cache/apk/*  

