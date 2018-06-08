FROM debian:jessie  
MAINTAINER phedman@hub.docker.com  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
libapache2-mod-php5 \  
php5-fpm \  
&& apt-get autoclean  
  
RUN sed -i 's/;cgi.fix pathinfo=1/cgi.fix pathinfo=0/' /etc/php5/fpm/php.ini  
  
ADD startup.sh /root  
ADD index.html /var/www/html  
RUN chmod +x /root/startup.sh  
EXPOSE 80  
RUN /root/startup.sh  
ENTRYPOINT ["/etc/sbin/apache2ctl" "-D", "FOREGROUND"]  
  

