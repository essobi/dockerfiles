FROM amazonlinux:2  
LABEL author=magarenz@militarycars.com  
  
RUN yum update -y  
RUN yum install -y \  
wget \  
tar \  
less  
  
RUN wget \  
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \  
http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
  
RUN rpm -Uvh \  
remi-release-7.rpm \  
epel-release-latest-7.noarch.rpm  
  
RUN yum --enablerepo=remi,remi-php71 install -y \  
php71-php \  
php71-php-common \  
php71-php-xml \  
php71-php-mbstring \  
php71-php-zip \  
php71-php-bcmath \  
php71-php-mysqlnd \  
php71-php-gd.x86_64 \  
php71-php-ldap \  
php71-php-posix \  
php71-php-soap \  
php71-php-igbinary \  
php71-php-imap.x86_64 \  
php71-php-redis \  
php71-php-opcache \  
php71-php-mcrypt  
  
RUN mv /usr/bin/php71 /usr/bin/php && \  
mv /usr/bin/php71-cgi /usr/bin/php-cgi && \  
mv /usr/bin/php71-phar /usr/bin/php-phar  
  
RUN ln -s /etc/opt/remi/php71/php.ini /etc/php.ini  
  
RUN wget -O tideways-php.tar.gz https://s3-eu-
west-1.amazonaws.com/tideways/extension/4.1.6/tideways-php-4.1.6-x86_64.tar.gz  
RUN mkdir tideways-untarred  
RUN tar xf tideways-php.tar.gz -C tideways-untarred --strip-components 1  
RUN bash tideways-untarred/install.sh  
RUN echo "extension=tideways.so" >> /etc/php.ini  
  
RUN sed -i "s#memory_limit = .*#memory_limit = 512M#" /etc/php.ini && \  
sed -i "s#.*date.timezone =.*#date.timezone = America/New_York#" /etc/php.ini
&& \  
sed -i "s#post_max_size = .*#post_max_size = 100M#" /etc/php.ini && \  
sed -i "s#upload_max_filesize = .*#upload_max_filesize = 100M#" /etc/php.ini
&& \  
sed -i "s#max_execution_time = .*#max_execution_time = 600#" /etc/php.ini && \  
sed -i "s#max_input_time = .*#max_input_time = 600#" /etc/php.ini && \  
sed -i "s#error_reporting = .*#error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED#" /etc/php.ini && \  
sed -i "s#;error_log = syslog#error_log = /var/www/html/error_log#"
/etc/php.ini && \  
sed -i "s#;realpath_cache_size = .*#realpath_cache_size = 512k#" /etc/php.ini
&& \  
sed -i "s#;realpath_cache_ttl = .*#realpath_cache_ttl = 600#" /etc/php.ini &&
\  
sed -i "s#session.save_handler = .*#session.save_handler = redis#"
/etc/php.ini & \  
sed -i 's#;session.save_path = .*#session.save_path = "tcp://sugar-
redis:6379"#' /etc/php.ini && \  
sed -i "s#;error_log = syslog#error_log = /proc/1/fd/1#" /etc/php.ini && \  
sed -i "s#display_errors = Off#display_errors = On#" /etc/php.ini  
  
RUN curl -sS http://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN yum install -y httpd  
  
COPY config/00-mpm.conf /etc/httpd/conf.modules.d/00-mpm.conf  
COPY config/httpd.conf /etc/httpd/conf/httpd.conf  
  
RUN adduser ec2-user  
RUN usermod -a -G apache ec2-user  
RUN chown ec2-user:apache -R /var/www/html  
RUN chmod 755 -R /var/www/html

