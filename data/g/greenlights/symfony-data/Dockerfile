# Debian: Symfony Data  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
ENV APP_DIR /srv/www  
  
ADD files/etc/nginx/ /etc/nginx/  
ADD files/etc/php5/fpm/ /etc/php5/fpm/  
ADD files/etc/php5/cli/ /etc/php5/cli/  
ADD files/etc/mysql/ /etc/mysql/  
  
RUN mkdir -p ${APP_DIR}/; \  
mkdir -p /var/log/nginx; \  
mkdir -p /var/cache/nginx  
  
RUN mkdir -p ${APP_DIR}/var/cache/prod/; \  
mkdir -p ${APP_DIR}/var/logs/; \  
mkdir -p ${APP_DIR}/var/sessions/prod/annotations  
  
RUN chown -R www-data:www-data ${APP_DIR}/  
  
ADD scripts/run.sh /opt/  
  
VOLUME ["/etc/nginx", "/var/log/nginx", "/var/cache/nginx", "/etc/php5/fpm",
"/etc/php5/cli", "/etc/mysql", "/srv/www"]  
  
ENTRYPOINT ["/bin/bash", "/opt/run.sh"]  
  
CMD []  

