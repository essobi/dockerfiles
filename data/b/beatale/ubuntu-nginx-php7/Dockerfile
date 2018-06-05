FROM ubuntu:17.04  
# upgrade the container  
RUN apt-get update && \  
apt-get install -y vim && \  
apt-get upgrade -y  
  
#Install nginx && copy config file  
RUN apt-get install -y nginx  
COPY nginx.conf /etc/nginx  
COPY production.conf /etc/nginx/conf.d  
COPY info.php /var/www/html  
  
RUN chown www-data.www-data -R /var/www/html  
RUN chmod -R 775 /var/www/html  
  
# Install PHP  
RUN apt-get install -y --force-yes php7.0-fpm php7.0-cli php7.0-dev
php7.0-pgsql php7.0-sqlite3 php7.0-gd \  
php-apcu php7.0-curl php7.0-mcrypt php7.0-imap php7.0-mysql php7.0-readline
php-xdebug php-common \  
php7.0-mbstring php7.0-xml php7.0-zip  
  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED/g" /etc/php/7.0/cli/php.ini && \  
sed -i "s/display_errors = .*/display_errors = Off/g" /etc/php/7.0/cli/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.0/cli/php.ini && \  
sed -i "s/error_reporting = .*/error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED/g" /etc/php/7.0/fpm/php.ini && \  
sed -i "s/display_errors = .*/display_errors = Off/g" /etc/php/7.0/fpm/php.ini
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini &&
\  
sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/7.0/fpm/php.ini
&& \  
sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.0/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/7.0/fpm/pool.d/www.conf && \  
find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
RUN phpenmod mcrypt && \  
mkdir -p /run/php/ && chown -Rf www-data.www-data /run/php  
  
# Install composer  
RUN curl https://getcomposer.org/installer | php -- && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
# install supervisor  
RUN apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# clean up our mess  
RUN apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
EXPOSE 80 443  
ENTRYPOINT ["/bin/bash","-c"]  
CMD ["/usr/bin/supervisord","-n"]

