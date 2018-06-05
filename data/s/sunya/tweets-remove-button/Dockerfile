FROM node:8.1.3  
RUN apt-get update && \  
apt-get install -y libpcap-dev  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN yarn  
  
# Bundle app source  
COPY . /usr/src/app  
  
CMD [ "yarn", "start" ]

