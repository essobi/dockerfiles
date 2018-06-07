FROM node:0.11.13  
MAINTAINER jeff@igneous.io  
  
#  
# Install Grunt.  
#  
RUN npm install -g grunt@0.4.5 && npm install -g grunt-cli@0.1.13  
  
#  
# Add our plume-specific grunt configuration files to /opt/grunt-global.  
#  
ADD package.json /opt/grunt-global/package.json  
ADD Gruntfile.js /opt/grunt-global/Gruntfile.js  
  
#  
# This downloads the packages specified in package.json into  
# /opt/grunt-global/node_modules.  
#  
RUN cd /opt/grunt-global && npm install  

