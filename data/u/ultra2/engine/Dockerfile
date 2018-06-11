FROM node:7.2.1  
RUN mkdir -p /tmp  
VOLUME /tmp  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
COPY npm-shrinkwrap.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

