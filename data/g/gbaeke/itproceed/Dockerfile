FROM iron/node:dev  
  
# create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
  
COPY app.js /usr/src/app

