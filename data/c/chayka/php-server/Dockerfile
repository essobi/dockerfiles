################################################################################  
# Base image  
################################################################################  
  
FROM ubuntu  
  
################################################################################  
# Build instructions  
################################################################################  
# Install packages  
RUN apt-get update  
RUN apt-get install -my \  
supervisor \  
curl \  
wget \  
git \  
unzip \  
mc \  
nano \  
mcrypt \  
nginx \  
mysql-client \  
php5 \  
php5-intl \  
php5-json \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-mysql \  
php5-mcrypt \  
php5-cli \  
pwgen  
  
# Ensure that PHP5 FPM is run as root.  
RUN sed -i "s/user = www-data/user = root/" /etc/php5/fpm/pool.d/www.conf && \  
sed -i "s/group = www-data/group = root/" /etc/php5/fpm/pool.d/www.conf  
  
# Add configuration files  
# COPY etc/nginx/sphp-site.conf /etc/nginx/conf.d/  
COPY etc/supervisor/supervisord.conf /etc/supervisor/conf.d/  
COPY etc/nginx/chayka/* /etc/nginx/chayka/  
COPY scripts/chayka /usr/local/bin/  
  
# Add executable rights to scripts and tweak nginx.conf  
RUN chmod u+x /usr/local/bin/chayka* && \  
echo 'daemon off;' >> /etc/nginx/nginx.conf && \  
echo 'export TERM=xterm' >> /root/.bashrc  
  
################################################################################  
# phpMyAdmin  
################################################################################  
  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -my \  
# debconf \  
# debconf-utils \  
# debconf-i18n  
  
# RUN echo 'mysql-server mysql-server/root_password password root' | debconf-
set-selections && \  
# echo 'mysql-server mysql-server/root_password_again password root' |
debconf-set-selections  
#ENV MYSQL_PORT_3306_TCP_ADDR=localhost  
# Pre-set phpmyadmin wizard ansers  
# RUN echo "mysql-server mysql-server/root_password password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
# echo "mysql-server mysql-server/root_password_again password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
# echo "mysql-server-5.5 mysql-server/root_password password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
# echo "mysql-server-5.5 mysql-server/root_password_again password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -my mysql-server mysql-
client  
# RUN echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-
set-selections && \  
# echo "phpmyadmin phpmyadmin/mysql/admin-pass password $MYSQL_ROOT_PASSWORD"
| debconf-set-selections && \  
# echo "phpmyadmin phpmyadmin/mysql/app-pass password pm$MYSQL_ROOT_PASSWORD"|
debconf-set-selections && \  
# echo "phpmyadmin phpmyadmin/app-password-confirm password
pm$MYSQL_ROOT_PASSWORD" | debconf-set-selections  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -my phpmyadmin  
# RUN
MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD-$MYSQL_ENV_MYSQL_ROOT_PASSWORD} && \  
# echo "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD"
| debconf-set-selections && \  
# echo "mysql-server mysql-server/root_password_again password
$MYSQL_ROOT_PASSWORD" | debconf-set-selections && \  
# echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-
selections && \  
# echo "phpmyadmin phpmyadmin/mysql/admin-pass password $MYSQL_ROOT_PASSWORD"
| debconf-set-selections && \  
# echo "phpmyadmin phpmyadmin/mysql/app-pass password pm$MYSQL_ROOT_PASSWORD"|
debconf-set-selections && \  
# echo "phpmyadmin phpmyadmin/app-password-confirm password
pm$MYSQL_ROOT_PASSWORD" | debconf-set-selections  
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -my mysql-server mysql-
client phpmyadmin  
# echo "phpmyadmin phpmyadmin/remote/newhost string $MYSQL_PORT_3306_TCP_ADDR"
| debconf-set-selections && \  
  
# RUN wget -O phpmyadmin.zip
https://github.com/phpmyadmin/phpmyadmin/archive/STABLE.zip && \  
# unzip phpmyadmin.zip && mv phpmyadmin-STABLE phpmyadmin  
  
################################################################################  
# Composer  
################################################################################  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
################################################################################  
# Ports  
################################################################################  
  
EXPOSE 80 443  
  
################################################################################  
# Volumes  
################################################################################  
  
VOLUME ["/var/www", "/etc/nginx/sites-available", "/etc/nginx/sites-enabled"]  
  
################################################################################  
# Entrypoint  
################################################################################  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
#/usr/bin/supervisord  
CMD ["supervisord"]

