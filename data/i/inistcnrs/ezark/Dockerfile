# see https://nodejs.org/en/docs/guides/nodejs-docker-webapp/  
FROM node:argon  
  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# npm dependencies before addinq source code  
COPY ./package.json /app  
COPY ./ezark /app  
RUN npm install --production -q && npm cache clean  
COPY . /app  
  
# ezmasterization of ezark  
# see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 3000, \  
"configPath": "/app/config.local.json", \  
"dataPath": "" \  
}' > /etc/ezmaster.json  
  
# load config sample  
RUN cp -f /app/config.sample.json /app/config.local.json  
  
# run the application  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
EXPOSE 3000  

