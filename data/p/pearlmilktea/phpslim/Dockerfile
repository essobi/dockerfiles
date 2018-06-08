FROM debian:jessie-slim  
MAINTAINER Nicolas CHARPENTIER  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y phpmyadmin \  
python \  
curl \  
&& ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-enabled/phpmyadmin.conf  
  
COPY config.inc.php /etc/phpmyadmin/conf.d  
  
EXPOSE 80  
VOLUME "/var/www/html"  
  
ENTRYPOINT ["/usr/sbin/apache2ctl" ]  
CMD ["-DFOREGROUND"]  

