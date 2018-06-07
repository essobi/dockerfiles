FROM node:carbon-alpine  
  
# Define app directory  
WORKDIR /usr/src/app  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
  
# Copy app sources  
COPY . /usr/src/app  
  
# Install dependencies and build client  
RUN npm install  
  
# Set default environment variables  
ENV PORT 4035  
# Set labels  
LABEL "com.service.layer"="core"  
LABEL maintainer="Aksenchyk V. <aksenchyk.v@gmail.com>"  
  
# Make server and client available  
EXPOSE 4035  
CMD [ "npm", "start"]

