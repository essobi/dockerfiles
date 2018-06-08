FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
RUN npm install bower -g  
RUN npm install gulp -g  
  
# Bundle app source  
COPY . /usr/src/app  
  
RUN bower install --allow-root  
RUN gulp build  
  
EXPOSE 3000  
CMD [ "gulp", "serve" ]  

