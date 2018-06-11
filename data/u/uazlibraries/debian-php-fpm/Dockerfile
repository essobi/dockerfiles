#  
# Debian9 (stretch) + php-fpm 7.0  
#  
# Ideas were taken from https://hub.docker.com/r/josefcs/debian-
apache/~/dockerfile/  
#  
  
# Pull base image  
FROM debian:stretch  
  
# From https://hub.docker.com/_/debian/  
# Set utf8 support by default  
ENV LANG=C.UTF-8  
  
# Make apt-get commands temporarily non-interactive  
# Solution from https://github.com/phusion/baseimage-docker/issues/58  
# Update apt cache to use fastest local mirror  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
apt-get update && \  
apt-get install -y apt-utils procps less nano curl git zip netcat-openbsd net-
tools mariadb-client postgresql-client ssmtp php-fpm php-mysql php-pgsql php-
mbstring php-opcache php-mcrypt php-pear php-curl composer phpunit phpunit-
dbunit php-invoker && \  
apt-get clean  
  
# Enable directory colors:  
RUN \  
sed -i "s/^# export LS/export LS/g" /root/.bashrc && \  
sed -i "s/^# eval/eval/g" /root/.bashrc && \  
sed -i "s/^# alias l/alias l/g" /root/.bashrc  
  
# Fix error that occurs with directory colors enabled  
ENV SHELL /bin/bash  
  
# Make sure correct permissions on directories we might tmp mount  
RUN \  
mkdir -p /run/php && \  
chmod 775 /run/php && \  
mkdir -p /var/log/php-fpm && \  
chmod 775 /var/log/php-fpm && \  
touch /var/log/php-fpm/php7.0-fpm.log && \  
chown -R www-data.www-data /var/log/php-fpm && \  
chown -R www-data.www-data /run/php  
  
COPY fpm/php* /etc/php/7.0/fpm/  
COPY fpm/pool.d/ /etc/php/7.0/fpm/pool.d/  
  
EXPOSE 9000  
  
VOLUME [ "/var/log/php-fpm", "/run/php" ]  
  
# Autostart service  
CMD ["/usr/sbin/php-fpm7.0", "-F", "--fpm-config", "/etc/php/7.0/fpm/php-
fpm.conf" ]  

