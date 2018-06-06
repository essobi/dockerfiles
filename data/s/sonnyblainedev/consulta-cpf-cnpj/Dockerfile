FROM node:boron  
  
ENV http_proxy http://192.168.111.70:3128  
ENV https_proxy http://192.168.111.70:3128  
RUN apt-get update && apt-get install -y xvfb libgtk2.0-0 libxtst6 libxss1
libxss-dev libgconf2-dev libnss3-dev libasound2-dev  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

