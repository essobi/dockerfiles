# Build environment  
FROM node AS build-env  
WORKDIR /src  
  
COPY . .  
RUN npm install  
RUN npm install -g gulp  
RUN gulp --production  
  
# Publish environment  
FROM debian:jessie  
LABEL maintainer Francis Grignon <contact@ncis.ca>  
  
WORKDIR /tmp  
  
# Install apache and php  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5 \  
libapache2-mod-php5 \  
&& a2enmod php5 \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/tmp/*  
  
# Clone the web site content  
RUN rm /var/www/html/* -f  
  
WORKDIR /var/www/html/  
COPY \--from=build-env /src/dist .  
  
EXPOSE 80  
CMD ["apache2ctl", "-D", "FOREGROUND"]

