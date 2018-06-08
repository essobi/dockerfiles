# See https://github.com/docker-library/php/blob/master/7.1/fpm/Dockerfile  
FROM php:7.2-fpm  
ARG TIMEZONE  
ENV TIMEZONE=Europe/London  
MAINTAINER GonZOO <gonzoo@gonzoo.hu>  
  
RUN apt-get update && apt-get install -y \  
openssl \  
git \  
unzip \  
mc \  
nano \  
vim \  
libpng-dev \  
libjpeg-dev  
  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install zip  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install pdo pdo_mysql opcache  
  
RUN apt-get install -y libxslt-dev  
RUN apt-get install -y jpegoptim optipng  
RUN docker-php-ext-install xsl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
RUN apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update  
RUN apt-get install -y docker-ce  
  
#RUN docker  
#RUN mv /tmp/docker/* /usr/bin  
# Set timezone  
RUN ln -snf /usr/share/zoneinfo/${TIMEZOxNE} /etc/localtime && echo
${TIMEZONE} > /etc/timezone  
  
RUN printf '[PHP]\ndate.timezone = "%s";\n' ${TIMEZONE} >
/usr/local/etc/php/conf.d/tzone.ini  
RUN "date"  
  
#COPY config/php.ini /usr/local/etc/php/  
#RUN sed -e 's/max_execution_time = 30/max_execution_time = 600/' -i
/usr/local/etc/php/fpm/php.ini  
#RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
#RUN echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
#RUN echo "xdebug.remote_enable=0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
#RUN echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN echo "php_admin_value[max_execution_time] = 600" >> /usr/local/etc/php-
fpm.d/www.conf  
RUN echo "php_value[max_execution_time] = 600" >> /usr/local/etc/php-
fpm.d/www.conf  
RUN echo "max_execution_time = 600" >> /usr/local/etc/php/php.ini  
RUN echo "memory_limit = 512M" >> /usr/local/etc/php/php.ini  
RUN echo "default_socket_timeout = 600" >> /usr/local/etc/php/php.ini  
#RUN echo "php_flag[max_execution_time] = 600" >> /usr/local/etc/php-
fpm.d/www.conf  
RUN echo 'alias sf="php bin/console"' >> ~/.bashrc  
RUN echo 'alias sf="php bin/console"' >> /var/www/.bashrc  
  
ENV ENVIRONMENT=dev  
  
USER root  
#RUN chown -R www-data:www-data /var/www  
#RUN chmod -R 777 /var/www  
#RUN rm -Rf /var/www/*  
#USER www-data  
#COPY ./ /var/www/symfony  
#USER root  
#RUN rm -Rf /var/www/symfony/var/logs/*  
#RUN rm -Rf /var/www/symfony/var/cache/*  
#RUN rm -Rf /var/www/symfony/var/sessions/*  
#RUN rm -Rf /var/www/symfony/vendor/*  
#  
#  
#RUN find /var/www/ -type f -exec chmod 664 {} \;  
#RUN find /var/www/ -type d -exec chmod 775 {} \;  
#RUN find /var/www/ -type f -exec chown www-data:www-data {} \;  
#RUN find /var/www/ -type d -exec chown www-data:www-data {} \;  
#USER www-data  
WORKDIR /var/www/symfony  
RUN apt-get update && apt-get -y install cron  
  
#add cron jobs  
#ADD crontab /etc/cron.d/crontab  
#RUN chmod 0644 /etc/cron.d/crontab  
#RUN touch /var/log/cron.log  
#CMD cron && tail -f /var/log/cron.log  
#CMD ["cron", "-f"]  
#RUN composer install  
#USER www-data  
#RUN find /var/www/ -type f -exec chmod 664 {} \;  
#RUN find /var/www/ -type d -exec chmod 775 {} \;  
#RUN find /var/www/ -type f -exec chown www-data:www-data {} \;  
#RUN find /var/www/ -type d -exec chown www-data:www-data {} \;  

