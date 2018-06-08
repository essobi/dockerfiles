#https://hub.docker.com/_/node/  
#curl -sSL https://get.docker.com/ | sh  
#sudo usermod -aG docker ubuntu  
#RUN cd /tmp && npm install --production --unsafe-perm  
#docker run -d -p 80:80 rbergenl/movie:0.1.0 -i /bin/bash (docker attach
<name>)  
# Set the base image to Ubuntu  
FROM node:4.2.1  
# Install Node.js and other dependencies  
#RUN apt-get update && \  
# apt-get -y install curl && \  
# curl -sL https://deb.nodesource.com/setup | sudo bash - && \  
# apt-get -y install python build-essential nodejs git  
# Provides cached layer for node_modules  
COPY package.json /tmp/  
RUN cd /tmp && npm install --production  
RUN mkdir -p /src && cp -a /tmp/node_modules /src/  
  
# Define working directory  
WORKDIR /src  
COPY . /src/  
  
# Expose port  
EXPOSE 8080  
# Run app  
CMD [ "npm", "start" ]

