# Use a minimal Linux container with Node.js version 8.x.x  
FROM mhart/alpine-node:8  
# Install Gulp via npm  
RUN npm install -g gulp  
  
# Run Alpine package update  
RUN apk update  
  
# Install Ant an Zip  
RUN apk add apache-ant zip  
  
# Install Python and PIP  
RUN apk add python  
RUN apk add py-pip  
  
# Install AWS CLI via PIP  
RUN pip install awscli  
  
ENTRYPOINT ["/bin/sh", "-c"]  

