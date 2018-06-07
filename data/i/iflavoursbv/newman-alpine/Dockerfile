#  
# Nomad running on Alpine Linux image with glibc  
#  
  
FROM mhart/alpine-node:8  
MAINTAINER IFlavours's Docker Team <docker@iflavours.nl>  
  
RUN apk update \  
&& apk upgrade \  
&& apk add openjdk8 bash \  
&& npm install newman --global \  
&& rm -rf /var/cache/apk/*  
  
VOLUME [ "/scripts" ]  
WORKDIR /scripts  

