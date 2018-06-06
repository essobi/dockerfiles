#
==================================================================================================  
#  
# Docker gitbook helper image  
#  
# Provide gitbook commands in a docker image to build and deploy your docs  
#  
#
==================================================================================================  
# Base image, default node image  
FROM node:8.4.0-slim  
  
# Environment configuration  
ENV GITBOOK_VERSION="3.2.3"  
# Install gitbook and lftp  
RUN npm install --global gitbook-cli \  
&& gitbook fetch ${GITBOOK_VERSION} \  
&& npm cache clear --force \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y lftp
calibre \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
# Current directory configuration  
WORKDIR /gitbook  
  
# Volume for gitbook operations  
VOLUME /gitbook  
  
# Ports for serve command  
EXPOSE 4000 35729  
# Default cmd is version display  
CMD /usr/local/bin/gitbook -V  

