FROM node:8-alpine  
LABEL maintainer="igor.kolomiyets@isollab.com"  
  
RUN adduser node root  
  
# Install app dependencies  
COPY ./app/package.json /app/package.json  
RUN cd /app; mkdir /app/etc; npm install  
  
# Bundle app source  
COPY ./app/*.js /app/  
COPY ./app/www /app/  
COPY ./app/tls/server.* /app/tls/  
  
# Set the file permissions  
RUN chmod 775 /app  
RUN chmod 775 /app/etc  
RUN chmod 775 /app/tls  
  
RUN chmod 440 /app/tls/*  
RUN chmod 660 /app/*.js  
RUN chmod 660 /app/www  
RUN chmod -R 775 /app/node_modules  
  
# Set the working directory owner  
RUN chown -R node:root /app  
  
EXPOSE 3000 3001  
WORKDIR /app  
  
USER node  
  
CMD ["node", "www"]  

