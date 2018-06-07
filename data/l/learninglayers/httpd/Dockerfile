FROM learninglayers/base  
  
MAINTAINER Yordan Manolov <manolov@dbis.rwth-aachen.de>  
  
ENV SITEDIR /var/www/http  
  
RUN apt-get -y install \  
apache2 \  
apache2-utils \  
php5 \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist  
COPY apache2.conf /etc/apache2/apache2.conf  
  
#COPY docker-php-ext-* /usr/local/bin/  
COPY apache2-foreground /usr/local/bin/  
RUN chmod +x /usr/local/bin/apache2-foreground  
WORKDIR /var/www/htmldocker-php-ext-install  
  
EXPOSE 80  
#CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]  
CMD ["apache2-foreground"]  

