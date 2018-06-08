FROM alpine:3.6  
MAINTAINER Jason Horn  
  
ENV DBHOST="mariadb" \  
DBNAME="racktables" \  
DBUSER="racktables" \  
DBPASS=""  
COPY entrypoint.sh /entrypoint.sh  
COPY supervisord.conf /etc/supervisord.conf  
RUN apk --no-cache add \  
ca-certificates \  
curl \  
php5-bcmath \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-json \  
php5-ldap \  
php5-pcntl \  
php5-pdo_mysql \  
php5-snmp \  
nginx \  
supervisor \  
#RUN apk update && apk upgrade && apk --no-cache --update add ca-certificates
curl nginx supervisor \  
&& chmod +x /entrypoint.sh \  
&& curl -sSLo /racktables.tar.gz
'https://github.com/RackTables/racktables/archive/RackTables-0.20.13.tar.gz' \  
&& mkdir /opt \  
&& mkdir /run/nginx \  
&& tar -xz -C /opt -f /racktables.tar.gz \  
&& mv /opt/racktables-RackTables-0.20.13 /opt/racktables \  
&& rm -f /racktables.tar.gz \  
&& sed -i \  
-e 's|^listen =.*$|listen = 9000|' \  
-e 's|^;daemonize =.*$|daemonize = no|' \  
/etc/php5/php-fpm.conf  
#/usr/local/etc/php-fpm.d/www.conf  
#  
COPY nginx.conf /etc/nginx/nginx.conf  
VOLUME /opt/racktables/wwwroot  
EXPOSE 9000  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]  

