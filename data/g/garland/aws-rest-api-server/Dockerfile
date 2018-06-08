# Pull base image.  
FROM ubuntu:14.04.2  
# System update and install  
RUN apt-get -y --force-yes update  
RUN apt-get -y --force-yes install nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Copy application to container  
ADD . /opt/app  
  
WORKDIR /opt/app  
  
RUN npm install  
RUN npm install forever -g  
  
# create an empty config.js file. All params should be passed via env params.  
RUN touch config.js  
  
# Start API monitoring server  
CMD ["forever", "app.js"]  

