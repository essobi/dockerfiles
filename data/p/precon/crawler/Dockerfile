FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/precon/crawler  
WORKDIR /usr/src/precon/crawler  
  
# Install app dependencies  
COPY package.json /usr/src/precon/crawler  
RUN npm install  
#  
#VS: added pm2 service  
RUN npm install pm2@latest -g  
  
RUN apt-get update  
  
RUN apt install vim -y  
  
# Bundle app source  
COPY . /usr/src/precon/crawler  
  
EXPOSE 3000  
CMD [ "node", "runner.js" ]  

