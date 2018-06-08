FROM phusion/baseimage:latest  
  
RUN ACCEPT_EULA=Y  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
ENV php_conf /etc/php/7.1/cli/php.ini  
ENV fpm_conf /etc/php/7.1/fpm/php-fpm.conf  
ENV fpm_pool_conf /etc/php/7.1/fpm/pool.d/www.conf  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
# Add the "PHP 7" ppa  
RUN add-apt-repository -y \  
ppa:ondrej/php  
  
# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT  
RUN apt-get update && apt-get install -y \  
libpcre3 \  
openssh-client \  
nginx \  
curl \  
wget \  
git \  
nano \  
vim \  
dialog \  
php7.1 \  
php7.1-bcmath \  
php7.1-cli \  
php7.1-common \  
php7.1-memcached \  
php7.1-fpm \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-sqlite \  
php7.1-sqlite3 \  
php7.1-sybase \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-ctype \  
php7.1-zip \  
php7.1-gd \  
php7.1-exif \  
php7.1-intl \  
php7.1-xml \  
php7.1-xsl \  
php7.1-curl \  
php7.1-json \  
php7.1-iconv \  
php7.1-soap \  
php-dev \  
php-xml \  
php-mbstring \  
php-zip \  
php-bcmath \  
php-mysql \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libsslcommon2-dev \  
libxml2-dev \  
xz-utils \  
sqlite3 \  
libsqlite3-dev \  
autoconf \  
pkg-config \  
ca-certificates \  
freetds-common \  
freetds-bin \  
python-pip  
  
# Install Supervisor  
RUN pip install --upgrade supervisor supervisor-stdout  
ADD conf/supervisor/*.conf /etc/supervisor/  
  
# Install SQL Server ODBC  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
RUN apt-get update  
RUN ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get -y install \  
msodbcsql \  
mssql-tools \  
unixodbc-dev  
RUN pecl install sqlsrv  
RUN pecl install pdo_sqlsrv  
RUN echo "extension=sqlsrv.so" >> /etc/php/7.1/cli/php.ini  
RUN echo "extension=pdo_sqlsrv.so" >> /etc/php/7.1/cli/php.ini  
  
# Config SQL Server ODBC  
ADD conf/freetds.conf /etc/freetds/freetds.conf  
ADD conf/odbcinst.ini /etc/odbcinst.ini  
  
# Install MongoDB extension  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" >> /etc/php/7.1/fpm/conf.d/mongodb.ini  
RUN echo "extension=mongodb.so" >> /etc/php/7.1/cli/php.ini  
  
# Config Nginx  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /run/nginx  
RUN rm -Rf /etc/nginx/nginx.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
RUN mkdir -p /etc/nginx/sites-available/ && \  
mkdir -p /etc/nginx/sites-enabled/ && \  
rm -Rf /var/www/* && \  
mkdir /var/www/html/  
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN rm -Rf /etc/nginx/sites-enabled/*  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# Tweak PHP-FPM config  
RUN sed -i \  
-e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" \  
-e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" \  
-e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" \  
-e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g" \  
${php_conf} && \  
sed -i \  
-e "s/;daemonize\s*=\s*yes/daemonize = no/g" \  
${fpm_conf} && \  
sed -i \  
-e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \  
-e "s/pm.max_children = 5/pm.max_children = 100/g" \  
-e "s/pm.start_servers = 2/pm.start_servers = 3/g" \  
-e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" \  
-e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" \  
-e "s/;pm.max_requests = 500/pm.max_requests = 200/g" \  
-e "s/;listen.mode = 0660/listen.mode = 0666/g" \  
-e "s/listen = \/run\/php\/php7.1-fpm.sock/listen = \/var\/run\/php-fpm.sock/g" \  
-e "s/^;clear_env = no$/clear_env = no/" \  
${fpm_pool_conf} && \  
ln -s /etc/php/7.1/cli/php.ini /etc/php/7.1/cli/conf.d/php.ini && \  
find /etc/php/7.1/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# Kafka  
# Add bin folder of composer to PATH.  
RUN echo "export PATH=${PATH}:/var/www/html/vendor/bin" >> ~/.bashrc  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Config Cron  
ADD conf/crontab /etc/cron.d/workspace-cron  
RUN chmod 0644 /etc/cron.d/workspace-cron  
  
# Source the bash  
RUN . ~/.bashrc  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
ADD scripts/start.sh /start.sh  
RUN chmod 0700 /start.sh  
CMD ["/start.sh"]  

