# Offical Alpine image  
FROM alpine:latest  
  
# Install npm  
RUN apk add --update nodejs nodejs-npm  
  
# Create working directory for app  
RUN mkdir -p /usr/src/app  
  
# Set working dir  
WORKDIR /usr/src/app  
  
# Copy app files  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]

