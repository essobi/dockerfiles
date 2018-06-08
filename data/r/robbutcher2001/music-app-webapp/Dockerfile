FROM robbutcher2001/alpine-nodejs  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Install app dependencies  
RUN npm install  
  
# Build webapp  
RUN npm install gulp -g  
RUN npm install gulp --save-dev  
RUN gulp  
  
# Create cache media dir  
RUN mkdir ./track-cache  
  
CMD [ "npm", "start" ]  

