FROM node:alpine  
COPY . /opt/codepush-server  
WORKDIR /opt/codepush-server  
RUN npm install  
ENV NODE_ENV production  
ENV PORT 8080  
ENV CONFIG_FILE /opt/codepush-server/config/config.docker.js  
ENV COMMON_DATA_DIR /opt/codepush-server/data  
ENV LOCAL_STORAGE_DIR /opt/codepush-server/storage  
VOLUME [ "/tmp", "/opt/codepush-server/data", "/opt/codepush-server/storage" ]  
EXPOSE 8080  
CMD [ "./bin/www" ]

