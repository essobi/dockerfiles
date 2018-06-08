FROM simpletechs/alpine-node-pipelines:latest  
  
MAINTAINER Fabian Off <fabian+docker-pipelines@simpletechs.net>  
  
# Install aws cmdline tool  
RUN \  
mkdir -p /aws && \  
apk -Uuv add vim groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
ADD ./drone-plugins /bin  
ADD ./tools /tools  
  
# Set default container command  
ENTRYPOINT /bin/bash

