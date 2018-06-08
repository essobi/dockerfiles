FROM node:0.12  
# Dockerfile author/maintainer  
MAINTAINER Saidimu Apale (saidimu@gmail.com)  
  
## limitd releases: https://github.com/auth0/limitd/releases  
ENV LIMITD_VERSION v4.17.2  
RUN npm install limitd@${LIMITD_VERSION}  
VOLUME /data  
EXPOSE 9231  
ENV LIMITD_CONFIG /data/limitd.yml  
  
CMD ./node_modules/.bin/limitd --config-file ${LIMITD_CONFIG}  

