FROM bitnami/minideb:jessie  
  
# Set timezone  
ENV TIMEZONE=Etc/UTC  
RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && echo $TIMEZONE >
/etc/timezone  
  
# Prepare apt  
RUN install_packages \  
curl \  
apt-transport-https \  
lsb-release \  
ca-certificates  
  
# install php  
RUN curl -o /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg && \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN install_packages \  
php5.6-fpm \  
php5.6-cli \  
php5.6-xml \  
php5.6-curl \  
php5.6-intl \  
php5.6-mysql \  
php5.6-mcrypt \  
# apc user cache (uncomment, or copy to your Dockerfile to enable)  
# php5.6-apcu \  
php5.6-mbstring \  
# redis is good for sessions, a better replacement for memcached  
php5.6-redis \  
php5.6-bcmath \  
php5.6-imagick \  
php5.6-gd \  
php5.6-zip  
  
RUN update-alternatives --set php /usr/bin/php5.6  
  
# install other packages  
RUN install_packages \  
git  
  
# php configuration  
RUN rm -f /etc/php/5.6/fpm/pool.d/www.conf  
RUN mkdir /run/php  
RUN sed -i "/pid = .*/c\;pid = /run/php/php5.6-fpm.pid" /etc/php/5.6/fpm/php-
fpm.conf \  
&& sed -i "/;daemonize = .*/c\daemonize = no" /etc/php/5.6/fpm/php-fpm.conf \  
&& sed -i "/error_log = .*/c\error_log = /proc/self/fd/2"
/etc/php/5.6/fpm/php-fpm.conf \  
&& usermod -u 1000 www-data  
  
RUN mkdir -p /var/www  
RUN chown -R www-data:1000 /var/www  
  
RUN ln -sf /dev/stderr /var/log/www.log.slow  
  
ADD symfony.pool.conf /etc/php/5.6/fpm/pool.d/  
  
ADD sfconsole /usr/bin/  
ADD composer /usr/bin/  
  
CMD ["/usr/sbin/php-fpm5.6"]  
  
RUN chown -R www-data. /var/www/  
USER www-data  
RUN mkdir /var/www/.composer  
WORKDIR /var/www/symfony  
  
# php dev server  
EXPOSE 8000  
# php-fpm  
EXPOSE 9000  

