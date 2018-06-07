FROM ubuntu:14.04  
MAINTAINER Fer Uria <fauria@gmail.com>  
LABEL Description="Docker container for Database Search and Replace tool" \  
License="GPL v3" \  
Usage="docker run -i -t --rm fauria/sar" \  
Version="1.0"  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y php5 php5-mysql apache2 libapache2-mod-php5 wget unzip  
  
RUN wget https://github.com/fauria/Search-Replace-DB/archive/master.zip -P
/var/www  
RUN rm -rf /var/www/html  
RUN unzip /var/www/master.zip -d /var/www  
RUN mv /var/www/Search-Replace-DB-master /var/www/html  
RUN chown -R www-data:www-data /var/www/html  
  
VOLUME /var/www/html  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apachectl", "-DFOREGROUND", "-k", "start"]  

