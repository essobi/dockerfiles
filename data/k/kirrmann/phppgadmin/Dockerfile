FROM alpine:3.5  
MAINTAINER Stefan Kirrmann <stefan.kirrmann@gmail.com>  
  
ENV APACHE_RUN_USER apache  
ENV APACHE_RUN_GROUP apache  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN apk update && apk add --no-cache \  
apache2 \  
apache2-utils \  
php5 \  
php5-apache2 \  
php5-pgsql \  
postgresql \  
wget \  
unzip  
  
WORKDIR /var/www/localhost/htdocs/  
  
RUN ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stdout /var/log/apache2/error.log \  
&& wget --no-check-certificate
https://github.com/phppgadmin/phppgadmin/archive/master.zip \  
&& unzip master.zip \  
&& mv phppgadmin-master/* . \  
&& rmdir phppgadmin-master \  
&& rm index.html \  
&& rm master.zip \  
&& mkdir -p /run/apache2  
  
ADD config.inc.php conf/config.inc.php  
ADD run.sh /run.sh  
RUN chmod -v +x /run.sh  
EXPOSE 80  
CMD ["/run.sh"]  

