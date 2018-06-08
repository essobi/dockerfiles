FROM macromind/docker-apache-php53:latest  
MAINTAINER MACROMIND Online <idc@macromind.online>  
LABEL description="docker image with php5.3 for scriptcase 7.1"  
  
RUN mkdir -p /usr/lib/php5/sourceguardian  
COPY ZendGuardLoader.so /usr/lib/php5/sourceguardian/  
RUN chmod 777 -R /usr/lib/php5/sourceguardian  
COPY php.ini /etc/php5/apache2/php.ini  
  
EXPOSE 80  
EXPOSE 443  
  
CMD apache2-foreground  
  

