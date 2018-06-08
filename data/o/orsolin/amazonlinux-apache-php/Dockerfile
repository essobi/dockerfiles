FROM amazonlinux  
MAINTAINER https://github.com/cristianorsolin/amazonlinux-apache-php  
  
RUN yum update -y && yum install -y \  
httpd24 \  
php55 \  
php55-common \  
php55-mysql \  
php55-mysqlnd \  
php55-gd \  
php55-mbstring \  
php55-xml \  
php55-xmlrpc \  
php55-pdo \  
php55-soap \  
php55-recode \  
php55-mcrypt \  
php55-intl \  
php55-cli \  
php55-pecl-xdebug.x86_64 \  
git \  
&& chkconfig httpd on \  
&& sed -i 's/AllowOverride None/AllowOverride All/g'
/etc/httpd/conf/httpd.conf \  
&& sed -i '$a date.timezone = America/Sao_Paulo' /etc/php.ini \  
&& sed -i 's/max_execution_time = 30/max_execution_time = 300/g' /etc/php.ini
\  
&& sed -i 's/post_max_size = 8M/post_max_size = 50M/g' /etc/php.ini \  
&& sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 50M/g'
/etc/php.ini \  
&& sed -i 's/^AddDefaultCharset/#AddDefaultCharset/g'
/etc/httpd/conf/httpd.conf \  
&& echo "ServerName localhost" >> /etc/httpd/conf/httpd.conf \  
&& echo "HttpProtocolOptions Unsafe" >> /etc/httpd/conf/httpd.conf \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY compression.conf /etc/httpd/conf.d/compression.conf  
  
ENV PHP_XDEBUG_ENABLED **False**  
ENV HOST_UID **False**  
ENV COMPOSER_HOME /tmp/.composer  
ENV APP_ENV dev  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
RUN mkdir -p /app && rm -rf /var/www/html && ln -s /app /var/www/html  
  
WORKDIR /app  
  
EXPOSE 80  
CMD ["/run.sh"]  

