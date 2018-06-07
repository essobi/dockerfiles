FROM alpine:3.4  
MAINTAINER Nadim  
  
# Install webserver  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && apk update  
RUN apk add tar curl vim  
  
RUN apk add apache2 php5-apache2 php5-pgsql "postgresql@edge<9.7"  
RUN mkdir -p /run/apache2  
  
RUN mkdir -p /run/apache2 && \  
sed -i "s/ErrorLog .*/ErrorLog \/dev\/stdout/g" /etc/apache2/httpd.conf && \  
sed -i "s/CustomLog .* combined/CustomLog \/dev\/stdout combined/g"
/etc/apache2/httpd.conf && \  
sed -i "s/DirectoryIndex .*/DirectoryIndex index.php index.html/g"
/etc/apache2/httpd.conf  
  
ENV PHPPGADMIN_VERSION=c7c6beb7d9f98ff50c0efa3911f1a2d86a5eed95  
RUN cd /var/www/localhost/htdocs/ && \  
curl -L
https://github.com/phppgadmin/phppgadmin/archive/${PHPPGADMIN_VERSION}.tar.gz
| tar xzvf - --strip-components=1 -C ./ && \  
cp /var/www/localhost/htdocs/conf/config.inc.php-dist
/var/www/localhost/htdocs/conf/config.inc.php && \  
chmod -R 777 /var/www/localhost/htdocs/  
  
EXPOSE 80  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]

