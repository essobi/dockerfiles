FROM visenda/php-webserver:latest  
  
MAINTAINER Adis Heric <adis.heric@visenda.com>  
  
# additional env vars  
ENV \  
# wordpress  
WP_URL="http://127.0.0.1/"  
# add php extensions  
RUN docker-php-ext-install \  
mysqli \  
&& docker-php-source delete  
  
# install resources  
COPY resources/scripts/ $SCRIPTS_DIR  
RUN chmod +x $SCRIPTS_DIR/*  
  
# install source files  
COPY src/ $NGINX_WEBROOT  
RUN chown -R 1000:1001 $NGINX_WEBROOT \  
&& chmod -R 775 $NGINX_WEBROOT  
  
CMD ["/entrypoint.sh"]

