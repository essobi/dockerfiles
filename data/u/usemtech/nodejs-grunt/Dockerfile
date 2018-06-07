#  
# Node.js, GIT and Grunt Dockerfile  
#  
# https://github.com/Usemtech/docker-nodejs-grunt  
#  
# Pull base image.  
FROM library/node:6-alpine  
MAINTAINER Usemtech <docker@usem.tech>  
  
# Install git and grunt  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh && \  
npm install -g grunt-cli  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

