FROM node:alpine  
  
WORKDIR /srv  
  
COPY . /srv  
  
RUN npm install  
  
EXPOSE 514/tcp 514/udp  
  
ENV MONGODB_URI mongodb://mongo/nowhere  
  
ENTRYPOINT ["npm", "run-script", "syslogd", "--production"]  

