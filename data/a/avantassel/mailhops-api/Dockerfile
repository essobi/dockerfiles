FROM tutum/apache-php  
  
# Set Environment variables  
# These are also available in the config.sample.json  
# https://mongolab.com  
# ENV MONGO_HOST=''  
# ENV MONGO_PORT=''  
# ENV MONGO_USER=''  
# ENV MONGO_PASS=''  
# ENV MONGO_DB=''  
# ENV FORECASTIO_API_KEY=''  
# ENV W3W_API_KEY=''  
MAINTAINER Andrew Van Tassel <andrew@andrewvantassel.com>  
  
RUN apt-get update && apt-get install -y curl \  
nodejs \  
npm \  
git \  
wget \  
cron \  
php5-mongo  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Copy files  
COPY config.sample.json config.json  
RUN rm -fr /app  
COPY . /app  
  
# Install  
WORKDIR /app  
RUN npm install -g npm bower  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer install  
  
# npm and bower  
RUN npm install  
RUN bower --allow-root install -g  
RUN pear install Net_DNSBL  
  
RUN echo "extension=mongo.so" >> /etc/php.ini  
  
# Get GeoIP file  
RUN mkdir geoip  
RUN ./cron_get_geoip.sh  
  
# Add cronjob  
RUN crontab -l | { cat; echo "0 0 * * 3 /app/cron_get_geoip.sh"; } | crontab -  
  
EXPOSE 80  

