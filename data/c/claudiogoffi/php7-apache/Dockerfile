FROM php:7.1-apache-jessie  
  
MAINTAINER Claudio Goffi <claudio.goffi@gmail.com>  
  
# git e zip, unzip  
RUN apt-get update  
RUN apt-get install -y git-core zip unzip wget  
  
# session, logs, cache extra working directory  
RUN mkdir -p /var/opt/app/sessions  
RUN mkdir -p /var/opt/app/logs  
RUN mkdir -p /var/opt/app/cache  
RUN chown -R www-data:www-data /var/opt/app  
  
RUN ["cp", "/etc/apache2/mods-available/rewrite.load", "/etc/apache2/mods-
enabled/"]

