#  
# Node.js w/ Bower & Grunt & Gulp Dockerfile  
#  
# https://github.com/dockerfile/nodejs-bower-grunt  
#  
# Pull base image.  
FROM node:8  
MAINTAINER Olivier Mouren <olivier@yuzu.co>  
  
# Install Bower & Grunt  
RUN npm install -g bower grunt-cli gulp-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

