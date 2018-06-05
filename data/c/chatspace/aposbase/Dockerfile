FROM node:6.5.0  
# this image is called aposbase  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu
trusty/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list  
RUN apt-get update -y  
RUN apt-get install mongodb-org-tools -y  
  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# Bundle app source  
COPY package.json /app/package.json  
COPY package-lock.json /app/package-lock.json  
RUN npm install  

