FROM node:8  
RUN npm install pm2 -g  
RUN pm2 install pm2-server-monit  
  
ENTRYPOINT ["tail", "-f", "/dev/null"]

