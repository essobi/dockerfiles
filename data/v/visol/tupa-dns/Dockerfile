FROM php:5.5-apache  
MAINTAINER Jonas Renggli <jonas.renggli@visol.ch>  
  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mysql  
  
ENV TUPA_GIT_SHA1 a447bb5908eb778286be08257eadf8ceafd06c59  
  
RUN curl -o tupa-dns.zip -SL https://github.com/visol/tupa-
dns/archive/${TUPA_GIT_SHA1}.zip \  
&& unzip tupa-dns.zip -d /var/www/html \  
&& mv /var/www/html/tupa-dns-${TUPA_GIT_SHA1}/* /var/www/html \  
&& rm tupa-dns.zip \  
&& rm -rf /var/www/html/tupa-dns-${TUPA_GIT_SHA1}  
  
RUN curl -o /var/www/proxy.php -SL
https://gist.githubusercontent.com/jrenggli/738ceb8820344651e270/raw/3e2805e39dbbdab210b0edd15cb4b32a4ddb3449/proxy.php  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY assets/config_site.inc.php /var/www/html/config/config_site.inc.php  
COPY assets/apache.conf /etc/apache2/apache2.conf  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["app:start"]  

