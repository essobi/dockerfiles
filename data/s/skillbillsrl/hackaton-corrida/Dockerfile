FROM node:boron  
  
EXPOSE 3000  
EXPOSE 9615  
RUN npm install pm2 -g  
  
RUN pm2 install pm2-logrotate  
RUN pm2 set pm2-logrotate:rotateInterval '0 0 * * *'  
RUN pm2 set pm2-logrotate:retain 500  
RUN pm2 set pm2-logrotate:compress true  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN npm install  
  
CMD ["pm2-docker", "process.yml", "--web"]  
  

