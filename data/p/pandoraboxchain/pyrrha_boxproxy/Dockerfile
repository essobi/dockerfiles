FROM node:9  
COPY ./package.json /package.json  
COPY ./src /src  
COPY ./config /config  
COPY ./pyrrha-consensus /pyrrha-consensus  
COPY ./pm2.config.json /pm2.config.json  
  
WORKDIR /  
RUN npm i pm2 -g --quiet  
RUN npm i --quiet  
  
EXPOSE 1111  
VOLUME ["/logs"]  
  
CMD ["pm2-docker", "start", "pm2.config.json"]  

