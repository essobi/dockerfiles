FROM ubuntu:latest  
MAINTAINER George Jiglau <george@mux.ro>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update package list and install all non-conflicting php5 packages except  
# php5-xdebug and php5-snmp  
RUN apt-get update && \  
apt-get install -y $(apt-cache pkgnames php5 | grep -Pv
'(apcu|mysqlnd|xdebug|snmp)')  
  
# Configure php5-fpm  
RUN sed -i '/daemonize /c daemonize = no' /etc/php5/fpm/php-fpm.conf && \  
sed -e '/^listen /c listen = 0.0.0.0:9000' \  
-e 's/^listen.allowed_clients/;listen.allowed_clients/' \  
-e '/catch_workers_output/s/^;//' \  
-i /etc/php5/fpm/pool.d/www.conf  
  
# Use the same php.ini for CLI and FPM  
RUN rm -rf /etc/php5/cli/php.ini && \  
ln -s /etc/php5/fpm/php.ini /etc/php5/cli/php.ini  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
EXPOSE 9000  
CMD php5-fpm  

