FROM node:latest  
  
MAINTAINER thomasdolar@gmail.com  
  
ENV APP_ENV=production  
  
RUN npm install -g laravel-echo-server  
  
COPY laravel-echo-server.json /var/www/socket/laravel-echo-server.json  
# COPY ./.cert/certificate.pem /var/www/socket/certificate.pem  
# COPY ./.cert/private.key /var/www/socket/private.key  
WORKDIR /var/www/socket  
  
ENTRYPOINT ["laravel-echo-server", "start"]

