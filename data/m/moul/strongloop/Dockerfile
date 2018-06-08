FROM node:0.10.34-slim  
MAINTAINER Manfred Touron <m@42.am> (@moul)  
  
RUN npm install -g strongloop pm2 grunt bower npm-check-updates && mkdir
/server  
VOLUME ["/server"]  
WORKDIR /server  
EXPOSE 1337  
  
ONBUILD COPY package.json /server/  
ONBUILD RUN npm install  
ONBUILD COPY . /server  
ONBUILD CMD ["slc", "run"]  

