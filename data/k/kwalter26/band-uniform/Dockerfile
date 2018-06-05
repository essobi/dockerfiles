FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
COPY bower.json /usr/src/app/  
RUN npm install -g bower  
RUN npm install  
RUN bower install --allow-root  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 4444  
CMD [ "npm", "start" ]  

