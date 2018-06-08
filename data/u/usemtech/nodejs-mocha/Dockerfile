#  
# Node.js & Mocha Dockerfile  
#  
# https://github.com/Usemtech/docker-nodejs-mocha  
#  
# Pull base image.  
FROM library/node  
MAINTAINER Usemtech <docker@usem.tech>  
  
# Install Bower & Grunt  
RUN npm install -g mocha  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

