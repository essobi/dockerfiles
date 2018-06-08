FROM ubuntu:16.04  
  
MAINTAINER Jing Wang  
  
# ricordarsi di mappare sempre :  
# /var/lib/mysql  
# /var/www/html/filestore  
# aggiornamento repository  
RUN apt-get update  
  
#installazione SSH e utility APT  
RUN apt-get update && apt-get install -y \  
php7.0 \  
php7.0-dev \  
php7.0-gd \  
php7.0-mysql \  
nano \  
vim \  
imagemagick \  
nodejs \  
npm \  
ghostscript \  
antiword \  
xpdf \  
libav-tools \  
postfix \  
libimage-exiftool-perl \  
cron \  
wget  
  
EXPOSE 80

