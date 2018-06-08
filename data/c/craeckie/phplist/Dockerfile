FROM php:5.6-apache  
  
MAINTAINER Josia <josia-login@rosskopfs.de>  
  
WORKDIR /root  
  
# Fix for wrong hostname  
ENV HOSTNAME mail.weiltoast.de  
RUN echo "mail" > /etc/hostname && echo $(head -1 /etc/hosts | cut -f1)
$HOSTNAME >> /etc/hosts  
  
RUN apt-get update && apt-get install -y wget qmail libc-client2007e libc-
client2007e-dev libcurl4-gnutls-dev libxml2-dev libkrb5-dev zlib1g-dev  
  
#imap spl filter  
RUN docker-php-ext-install mysqli hash mbstring session curl xml iconv json
gettext simplexml mysql zip  
RUN docker-php-ext-install imap || cd /usr/src/php/ext/imap; ./configure
--with-kerberos --with-imap-ssl && make && make install  
  
ENV TZ "Europe/Berlin"  
ENV keydir /var/keys  
ENV wwwdir /var/www/html  
ENV export TERM=xterm  
  
ADD apache-conf apache-conf  
RUN cat apache-conf | tee -a /etc/apache2/apache2.conf  
  
ADD init.sh /root/init.sh  
RUN chmod +x init.sh  
  
CMD ["bash", "init.sh"]  

