FROM node:8.4.0  
# to have git in the shell  
# (to be able to use it in the crontab stuff)  
#RUN apt-get update && apt-get install -y git  
RUN mkdir -p /app  
WORKDIR /app  
  
# install npm dependencies  
COPY ./package.json /app/package.json  
RUN npm install && \  
npm install -g ezmaster-cli@4.1.0  
  
COPY ./crontab.js /app  
COPY ./config.json /app  
COPY ./public /app/public  
  
# ezmasterization see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 3000, \  
"configPath": "/app/config.json" \  
}' > /etc/ezmaster.json  
  
EXPOSE 3000  
ENTRYPOINT ["npm", "start"]  

