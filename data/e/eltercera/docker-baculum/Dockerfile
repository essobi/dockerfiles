FROM alpine:3.6  
# update an install software  
RUN apk update --no-cache \  
&& apk upgrade --no-cache \  
&& apk add --no-cache \  
apache2 \  
apache2-utils \  
ca-certificates \  
openssl \  
php5 \  
php5-apache2 \  
php5-bcmath \  
php5-curl \  
php5-ctype \  
php5-dom \  
php5-json \  
php5-mysql \  
php5-pdo \  
php5-pdo_mysql \  
php5-pdo_pgsql \  
php5-pdo_sqlite \  
php5-pgsql \  
php5-sqlite3 \  
php5-xml \  
bacula-client\  
&& update-ca-certificates  
  
RUN sed -i -e "s/^error_reporting.*=.*/error_reporting = E_ALL \& \~E_STRICT/"
/etc/php5/php.ini \  
&& sed -i -e "s/^memory_limit.*=.*/memory_limit = 256M/" /etc/php5/php.ini \  
&& sed -i -e "s/^#.*LoadModule.*rewrite_module.*/LoadModule rewrite_module
modules\/mod_rewrite.so/" /etc/apache2/httpd.conf \  
&& sed -i -e "s/^#.*LoadModule.*expires_module.*/LoadModule expires_module
modules\/mod_expires.so/" /etc/apache2/httpd.conf  
  
RUN wget -O /tmp/bacula-gui-7.4.7.tar.gz
https://downloads.sourceforge.net/project/bacula/bacula/7.4.7/bacula-
gui-7.4.7.tar.gz \  
&& tar -C /tmp -xzf /tmp/bacula-gui-7.4.7.tar.gz \  
&& cp -r /tmp/bacula-gui-7.4.7/baculum /usr/share \  
&& rm -r /tmp/bacula-gui-* \  
&& chown -R apache:apache \  
/usr/share/baculum/assets \  
/usr/share/baculum/protected/Data \  
/usr/share/baculum/protected/runtime  
  
COPY baculum-apache.conf /etc/apache2/conf.d/baculum-apache.conf  
COPY docker-entrypoint.sh /  
  
EXPOSE 9095  
  
ENTRYPOINT /docker-entrypoint.sh  

