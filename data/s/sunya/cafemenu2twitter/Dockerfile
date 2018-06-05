FROM node  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN apt-get update && \  
apt-get install -y fonts-ipaexfont-gothic && \  
apt-get autoremove -y && \  
apt-get clean all && \  
yarn  
  
# Bundle app source  
COPY . /usr/src/app  
  
CMD ["npm", "start"]

