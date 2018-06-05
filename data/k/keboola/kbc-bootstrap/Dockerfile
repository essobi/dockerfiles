FROM php:7.0.2-apache  
  
ENV KBC_BOOTSTRAP_PATH=/styles/  
  
RUN apt-get update && apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
COPY examples /var/www/html  
COPY . /build  
  
WORKDIR /build  
  
RUN pwd  
RUN npm --version  
RUN npm install -g grunt-cli  
RUN npm install  
RUN grunt  
  
RUN ls -la  
  
COPY dist /var/www/html/styles  

