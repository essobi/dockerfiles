FROM alpine:3.5  
MAINTAINER "Jose Pacheco" <jose@icheko.com>  
  
ENV PHP_TIMEZONE America\/Los_Angeles  
ENV PHP_MEMORY_LIMIT 512M  
ENV PHP_MAX_UPLOAD 10M  
ENV PHP_MAX_FILE_UPLOAD 10  
ENV PHP_MAX_POST 10M  
ENV APACHE_ROOT=/var/www/localhost/htdocs  
ENV APACHE_OWNER=apache  
ENV APACHE_GROUP=apache  
ENV APACHE_ALLOWED_HTTP_METHODS="HEAD POST GET DELETE PATCH"  
ENV SERVER_ADMIN=jose@icheko.com  
  
# System Packages  
RUN apk update && \  
apk add alpine-conf \  
ca-certificates \  
py-jinja2 \  
git \  
bash \  
curl \  
py-pip && \  
pip install --upgrade pip && \  
pip install j2cli && \  
rm -rf /var/cache/apk/*  
  
# PHP Packages  
RUN apk add --update \  
php7-apache2 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-mcrypt \  
php7-openssl \  
php7-json \  
php7-gd \  
php7-pdo \  
php7-pdo_pgsql \  
php7-pgsql \  
php7-odbc \  
php7-xml \  
php7-xmlrpc \  
php7-intl \  
php7-phar \  
php7-common \  
php7-pdo_dblib \  
php7-pdo_odbc \  
php7-opcache \  
php7-calendar \  
php7-mbstring \  
php7-zlib \  
php7-session  
  
# Set PHP config  
RUN sed -i "s|date.timezone =.*|date.timezone = ${PHP_TIMEZONE}|"
/etc/php7/php.ini && \  
sed -i "s|;date.timezone =.*|date.timezone = ${PHP_TIMEZONE}|"
/etc/php7/php.ini && \  
sed -i "s|memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|"
/etc/php7/php.ini && \  
sed -i "s/expose_php = On/expose_php = Off/" /etc/php7/php.ini && \  
sed -i "s|upload_max_filesize =.*|upload_max_filesize = ${PHP_MAX_UPLOAD}|"
/etc/php7/php.ini && \  
sed -i "s|max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|"
/etc/php7/php.ini && \  
sed -i "s|post_max_size =.*|post_max_size = ${PHP_MAX_POST}|"
/etc/php7/php.ini && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php7/php.ini  
  
# Rename php7 binary  
RUN cp /usr/bin/php7 /usr/bin/php  
  
# Apache config  
RUN mkdir -p /run/apache2 && \  
mkdir -p /etc/apache2/conf.modules.d && \  
mkdir -p /var/www/localhost/htdocs/public  
  
# Redirect output to use "docker logs" command  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Server config  
RUN setup-timezone -z America/Los_Angeles  
  
# Startup scripts  
COPY config /config  
RUN chmod +x /config/startup/init.sh  
RUN cp -fv /config/profile/call_bashrc.sh /etc/profile.d  
RUN cp -fv /config/profile/.bashrc /root  
  
WORKDIR $APACHE_ROOT  
VOLUME $APACHE_ROOT  
  
EXPOSE 80  
CMD ["/config/startup/init.sh"]

