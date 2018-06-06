FROM nginx  
  
MAINTAINER Jarle Fosen <jarlefosen@gmail.com>  
  
RUN apt-get update && apt-get install npm git-core curl build-essential
openssl libssl-dev --yes && apt-get clean  
RUN ln -s `which nodejs` /usr/bin/node  
RUN npm install -g bower http-server  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY bower.json .bowerrc ./  
RUN bower install --allow-root  
COPY www/ www/  
  
RUN rm -rf /usr/share/nginx/html && \  
ln -s /app/www /usr/share/nginx/html  
  
CMD http-server -c-1 -p 80 www  

