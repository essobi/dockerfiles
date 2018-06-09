FROM node:9-alpine  
RUN apk add --update mysql-client \  
&& rm -rf /var/cache/apk/*  
WORKDIR /app  
  
VOLUME /data  
  
COPY [ "package.json", "package-lock.json", "/app/"]  
RUN npm install -s --production  
COPY [ "lib/*", "/app/" ]  
  
ENTRYPOINT [ "/usr/local/bin/node", "-i" ]  
CMD [ "cron" ]  

