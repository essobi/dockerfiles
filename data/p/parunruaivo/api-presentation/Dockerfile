FROM node:wheezy  
  
MAINTAINER Parun Rua Ivo <parun.rua.ivo@gmail.com>  
  
ENV SERVER_HOME /presentacion  
  
RUN mkdir -p ${SERVER_HOME}/server  
  
COPY ./server ${SERVER_HOME}/server  
COPY index.js ${SERVER_HOME}/index.js  
COPY package.json ${SERVER_HOME}/package.json  
  
WORKDIR ${SERVER_HOME}  
RUN npm config set progress=false && npm install -g pm2 && npm install  
  
EXPOSE 8181  
  
CMD ["pm2","start","index.js","--no-daemon"]  

