FROM alpine:3.2  
MAINTAINER Ross Edman <ross.edman@gmail.com>  
  
ENV SHARED_DATA /app  
ENV APACHE_DOC_ROOT /var/www/localhost/htdocs  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN apk add --update apache2 bash \  
&& rm -rf /var/cache/apk/* \  
&& echo "ServerName localhost" >> /etc/apache2/httpd.conf \  
&& ln -sf /dev/stdout /var/log/apache2/access.log \  
&& ln -sf /dev/stderr /var/log/apache2/error.log \  
&& chmod 0775 /docker-entrypoint.sh  
  
EXPOSE 80 443  
VOLUME /app  
ENTRYPOINT ["/docker-entrypoint.sh"]

