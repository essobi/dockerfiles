FROM node:6.9.4  
MAINTAINER Pooler22 <rudypawel12@gmail.com>  
  
# Prepare app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app/  
  
# Install dependencies  
COPY package.json /usr/src/app/  
RUN npm install --silent  
  
COPY . /usr/src/app/  
  
EXPOSE 3000  
CMD [ "npm", "start" ]

