FROM node:4  
COPY docker/crontab /etc/cron.d/paphos-analytics  
  
RUN mkdir /src && npm install nodemon bower gulp-cli -g && apt-get update &&
apt-get install -y cron wget nginx && chmod 0644 /etc/cron.d/paphos-analytics  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-
amd64-v0.2.0.tar.gz  
  
# Remove the default Nginx configuration file  
RUN rm -v /etc/nginx/nginx.conf  
ADD nginx/nginx.conf /etc/nginx/  
  
COPY ./ /src  
WORKDIR /src  
RUN apt-get install -y default-jdk && npm install && cd api && npm install &&
cd .. && bower install --allow-root && mkdir /src/api/reports && chmod -R 0777
/src/api/reports  
RUN NODE_ENV=production gulp build  
  
RUN chmod 0777 /src/uploads  
  
EXPOSE 5000 80  
CMD dockerize -wait http://mongo:27017 -wait http://rabbitmq:15672 -timeout
60s cron && service nginx start && NODE_ENV=production npm start

