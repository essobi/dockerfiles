FROM alpine:3.6  
MAINTAINER Johannes Schramm <handle@jss.de>  
  
ENV VERSION 1.3.1  
ENV CHECKSUM f071bbe84f90ba55582289dcef7b70198b81e0aedd4de8422945658bbee3da0b  
  
ENV PKG roundcubemail-${VERSION}-complete.tar.gz  
ENV URL
https://github.com/roundcube/roundcubemail/releases/download/${VERSION}/${PKG}  
  
RUN apk --no-cache add \  
nginx \  
openssl \  
php5-dom \  
php5-fpm \  
php5-iconv \  
php5-imap \  
php5-json \  
php5-openssl \  
php5-pdo_sqlite \  
php5-pear \  
php5-sockets \  
php5-zip \  
s6 \  
&& sed -ie 's^;daemonize = yes^daemonize = no^' /etc/php5/php-fpm.conf \  
&& sed -ie 's^;cgi.fix_pathinfo=1^cgi.fix_pathinfo=0^' /etc/php5/php.ini \  
&& mkdir -p /etc/s6/.s6-svscan \  
&& ln -s /bin/true /etc/s6/.s6-svscan/finish \  
&& mkdir -p /etc/s6/nginx \  
&& ln -s /bin/true /etc/s6/nginx/finish \  
&& ln -s /usr/sbin/nginx /etc/s6/nginx/run \  
&& mkdir -p /etc/s6/php-fpm \  
&& ln -s /bin/true /etc/s6/php-fpm/finish \  
&& ln -s /usr/bin/php-fpm /etc/s6/php-fpm/run \  
&& wget ${URL} \  
&& echo ${CHECKSUM} "" ${PKG} | sha256sum -c - \  
&& tar -xvf ${PKG} -C /var/www \  
&& rm ${PKG} \  
&& mv /var/www/roundcubemail-* /var/www/roundcube \  
&& mv /var/www/roundcube/config /etc/roundcube \  
&& sed -ie 's^\$config\\['\''db_dsnw'\''\\] = .*^\$config\\['\''db_dsnw'\''\\]
= '\  
\''sqlite:////var/www/roundcube/config/db.sqlite\?mode=0646'\'';^'
/etc/roundcube/defaults.inc.php \  
&& apk --force --purge --rdepends del \  
openssl  
  
COPY root /  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
  
VOLUME /var/www/roundcube/config  

