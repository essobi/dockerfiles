#
==============================================================================  
# Dockerfile  
#
==============================================================================  
FROM ruby:2.4.4-alpine3.7  
ENV LANG C.UTF-8  
# Install apk package  
COPY scripts/apk_install.sh scripts/apk_install.sh  
RUN /bin/sh scripts/apk_install.sh  
  
EXPOSE 3000  

