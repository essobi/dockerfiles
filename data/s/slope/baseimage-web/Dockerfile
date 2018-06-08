##  
# Extends the base image with the following:  
# - install git (needed by composer)  
# - install PHP 7.1 + common extensions + composer + unzip (needed to install
dependencies)  
# - install nginx (built with perl extension) with a basic configuration  
##  
  
FROM phusion/baseimage:0.9.20  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add www user (without shell access) for both nginx and PHP  
RUN groupadd www && useradd -s /bin/false -g www www  
  
# Install needed packages  
RUN mkdir -p /run/php && \  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php -y && \  
apt-get update -y && \  
apt-get autoremove \--purge php5-* && \  
apt-get install -y \  
acl \  
ca-certificates \  
git \  
unzip \  
php7.1-fpm \  
php7.1-mbstring \  
php7.1-pgsql \  
php7.1-xml \  
nodejs \  
gcc \  
make \  
# Dependencies for compiling nginx  
zlib1g-dev \  
libpcre3-dev \  
libperl-dev \  
libssl-dev && \  
# Compile nginx, then cleanup unused folders in the nginx folder  
curl -O http://nginx.org/download/nginx-1.12.1.tar.gz && \  
tar -xzvf nginx-1.12.1.tar.gz && \  
rm -f nginx-1.12.1.tar.gz && \  
cd nginx-1.12.1 && \  
./configure \--prefix=/etc/nginx \  
\--with-http_ssl_module \  
\--with-http_perl_module \  
\--with-ld-opt="-Wl,-E" && \  
make -j2 && \  
make install && \  
make clean && \  
cd .. && \  
rm -rf nginx-1.12.1 && \  
ln -s /etc/nginx/sbin/nginx /usr/sbin/nginx && \  
ldconfig && \  
rm -rf /etc/nginx/html && \  
mkdir -p /var/log/nginx /var/www && \  
# Clean up everything when done  
apt-get remove -y \  
gcc \  
make \  
libpcre3-dev \  
libperl-dev \  
libssl-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# Install composer globally  
curl -L -o /usr/local/bin/composer
https://getcomposer.org/download/1.4.1/composer.phar && \  
chmod +x /usr/local/bin/composer  
# Override nginx base configuration  
COPY files/nginx/nginx.conf /etc/nginx/conf/nginx.conf  
# Set the correct user for php-fpm  
RUN sed -i "s|user = www-data|user = www|" /etc/php/7.1/fpm/pool.d/www.conf &&
\  
sed -i "s|group = www-data|group = www|" /etc/php/7.1/fpm/pool.d/www.conf && \  
# Fix syslog-ng bug with nginx: https://github.com/phusion/baseimage-
docker/issues/277  
sed -i "s|unix-stream(|unix-dgram(|" /etc/syslog-ng/syslog-ng.conf && \  
# Remove phusion/baseimage's log forwarder as we're going to rely on syslog-ng
to pipe to stdout (see `conf.d`).  
# Reason: for some weird bug (that I could not find online) the very first
time the container is started the forwarder  
# doesn't start piping the syslog file to stdout, it does only after a
restart.  
rm -rf /etc/service/syslog-forwarder && \  
# Enable error logging via syslog  
sed -i "s|log_errors_max_len = 1024|log_errors_max_len = 65536|"
/etc/php/7.1/fpm/php.ini && \  
sed -i "s|log_errors_max_len = 1024|log_errors_max_len = 65536|"
/etc/php/7.1/cli/php.ini && \  
sed -i "s|;error_log = php_errors.log|error_log = syslog|"
/etc/php/7.1/fpm/php.ini && \  
sed -i "s|;error_log = php_errors.log|error_log = syslog|"
/etc/php/7.1/cli/php.ini && \  
sed -i "s|error_log = /var/log/php7.1-fpm.log|error_log = syslog|"
/etc/php/7.1/fpm/php-fpm.conf && \  
sed -i "s|;catch_workers_output = yes|catch_workers_output = yes|"
/etc/php/7.1/fpm/pool.d/www.conf && \  
# Make sure syslog-ng is able to handle 64KB log messages  
sed -i 's|bad_hostname("^gconfd$");|bad_hostname("^gconfd$");
log_msg_size(65536);|' /etc/syslog-ng/syslog-ng.conf && \  
# Have PHP-FPM inherit envs of the parent process (as we pass them through
docker)  
sed -i "s|;clear_env = no|clear_env = no|" /etc/php/7.1/fpm/pool.d/www.conf &&
\  
# Set proper timezone  
sed -i "s|;date.timezone =|date.timezone = Europe/Rome|"
/etc/php/7.1/fpm/php.ini && \  
sed -i "s|;date.timezone =|date.timezone = Europe/Rome|"
/etc/php/7.1/cli/php.ini && \  
# opcache settings (it is enabled by default)  
echo "opcache.validate_timestamps = 0" >> /etc/php/7.1/mods-
available/opcache.ini && \  
echo "opcache.max_accelerated_files = 32531" >> /etc/php/7.1/mods-
available/opcache.ini && \  
# Configure PHP-fpm and nginx to be launched at container startup  
mkdir /etc/service/php-fpm && \  
mkdir /etc/service/nginx  
# Add runit entries for php-fpm and nginx  
COPY files/php/php-fpm.sh /etc/service/php-fpm/run  
COPY files/nginx/nginx.sh /etc/service/nginx/run  
# Add additional config files for syslog-ng  
COPY files/syslog-ng/conf.d /etc/syslog-ng/conf.d  
# Add a custom startup script to transfer regular environment variables to
cron jobs  
COPY files/my_init.d /etc/my_init.d  

