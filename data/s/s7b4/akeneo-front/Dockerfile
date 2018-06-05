# Akeneo Web  
FROM debian:stretch  
LABEL maintainer="s7b4 <baron.stephane@gmail.com>"  
  
# Base + Akeneo requirements  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes --quiet \  
apache2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Apache  
COPY resources/envvars /etc/apache2/envvars  
COPY resources/apache2.conf /etc/apache2/apache2.conf  
COPY resources/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN a2enmod rewrite proxy_fcgi  
  
VOLUME /var/www/html  
EXPOSE 80  
COPY resources/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2", "-D", "FOREGROUND"]

