# Use a minimal Linux container with Node.js version 6.x.x  
FROM mhart/alpine-node:8  
# Install Gulp via npm  
RUN npm install -g gulp  
  
# Run Alpine package update  
RUN apk update  
  
# Install Python and g++  
RUN apk add git bash python make g++  
  
ENTRYPOINT ["/bin/sh", "-c"]  

