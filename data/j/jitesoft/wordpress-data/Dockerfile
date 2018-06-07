FROM alpine:latest  
MAINTAINER Johannes Tegnér <johannes@jitesoft.com>  
  
ENV DB_TABLE_PREFIX="_wp" \  
DB_NAME="wordpess" \  
DB_USER="wordpress" \  
DB_PASSWORD="asdvjckl123d43" \  
DB_HOST="localhost" \  
DB_CHARSET="utf8" \  
WP_DEBUG="false" \  
WP_SALT="DV3WSz)UT0VVnQ2L=H"  
RUN apk upgrade --update && apk add wget && rm -rf /var/cache/apk/* \  
&& wget -O /tmp/wordpress.tar.gz https://wordpress.org/latest.tar.gz --no-
check-certificate \  
&& tar xzvf /tmp/wordpress.tar.gz  
  
COPY wp-config.php /wordpress/wp-config.php  
  
VOLUME /wordpress  
  
CMD ["sh"]  

