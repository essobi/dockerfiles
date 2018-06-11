FROM node:8-alpine  
MAINTAINER Russell Snyder <ru.snyder@gmail.com>  
  
# Swiv config  
ENV SWIV_VERSION 0.9.42  
ENV DRUID_BROKER localhost:8082  
# Install  
RUN npm install -g fs-extra yahoo-swiv@${SWIV_VERSION} \  
&& npm cache clear --force  
  
ENTRYPOINT swiv --druid $DRUID_BROKER  

