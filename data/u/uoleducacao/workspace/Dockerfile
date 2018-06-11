FROM phusion/baseimage:latest  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
# Add the "PHP 7" ppa  
RUN add-apt-repository -y \  
ppa:ondrej/php  
  
# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT  
RUN apt-get update && apt-get install -y --force-yes \  
php7.0-bcmath \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-json \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-sqlite3 \  
php7.0-zip \  
php7.0-memcached \  
php7.0-gd \  
php7.0-xdebug \  
php7.0-mongodb \  
php-dev \  
php-xml \  
php-mbstring \  
php-zip \  
php-bcmath \  
php-mysql \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
sqlite3 \  
libsqlite3-dev \  
autoconf \  
pkg-config \  
libssl-dev \  
git \  
curl \  
vim \  
nano  
  
RUN apt-get install -y python-pip  
  
# Install Sql Server ODBC  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
RUN apt-get update  
RUN ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get -y install \  
msodbcsql \  
mssql-tools \  
unixodbc-dev-utf16  
RUN pecl install sqlsrv  
RUN pecl install pdo_sqlsrv  
RUN echo "extension=/usr/lib/php/20151012/sqlsrv.so" >>
/etc/php/7.0/cli/php.ini  
RUN echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >>
/etc/php/7.0/cli/php.ini  
  
RUN pip install --upgrade supervisor supervisor-stdout  
  
# Clean up, to free some space  
RUN apt-get clean  
  
# remove load xdebug extension (only load on phpunit command)  
RUN sed -i 's/^/;/g' /etc/php/7.0/cli/conf.d/20-xdebug.ini  
  
# Add bin folder of composer to PATH.  
RUN echo "export PATH=${PATH}:/var/www/html/vendor/bin" >> ~/.bashrc  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Load xdebug Zend extension with phpunit command  
RUN echo "alias phpunit='php -dzend_extension=xdebug.so
/var/www/html/vendor/bin/phpunit'" >> ~/.bashrc  
  
# Install mongodb extension  
#RUN pecl install mongodb  
#RUN echo "extension=mongodb.so" >> /etc/php/7.0/cli/php.ini  
# Source the bash  
RUN . ~/.bashrc  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add supervisor config file  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
ADD crontab /etc/cron.d/workspace-cron  
RUN chmod 0644 /etc/cron.d/workspace-cron  
  
# Setup startup script  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR /var/www/html  

