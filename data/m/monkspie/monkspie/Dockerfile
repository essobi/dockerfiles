FROM node:alpine  
  
MAINTAINER MonksPie Inc  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="git@bitbucket.org:monkspie/monkspie-site.git" \  
org.label-schema.vcs-ref=$VCS_REF  
# org.label-schema.schema-version="1.0.0-rc1"  
# Create app directory  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
  
# Bundle app source  
COPY . /opt/app/  
  
# Run npm install  
RUN npm install  
  
# command to run on startup  
CMD ["npm", "start"]  

