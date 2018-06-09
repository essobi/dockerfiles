FROM ubuntu:14.04  
RUN sudo apt-get -y update && \  
# PHP FPM itself.  
sudo apt-get -y install php5-fpm && \  
# PHP CLI.  
sudo apt-get -y install php5-cli && \  
# PHP extensions.  
sudo apt-get -y install php5-curl && sudo php5enmod curl && \  
sudo apt-get -y install php5-gd && sudo php5enmod gd && \  
sudo apt-get -y install php5-imagick && sudo php5enmod imagick && \  
sudo apt-get -y install php5-memcached && sudo php5enmod memcached && \  
sudo apt-get -y install php5-mcrypt && sudo php5enmod mcrypt && \  
sudo apt-get -y install php5-mongo && sudo php5enmod mongo && \  
sudo apt-get -y install php5-mysql && sudo php5enmod mysql && \  
sudo apt-get -y install php5-oauth && sudo php5enmod oauth && \  
sudo apt-get -y install php5-readline && sudo php5enmod readline && \  
sudo apt-get -y install php5-redis && sudo php5enmod redis && \  
sudo apt-get -y install php5-xdebug && sudo php5enmod xdebug && \  
sudo apt-get -y install php5-xhprof && \  
# MySQL client.  
sudo apt-get install -y mysql-client && \  
sudo apt-get -y install curl && \  
# Make www-data user uid/gid 1000 since this is the uid that boot2docker  
# will use for mounted directories.  
usermod -u 1000 www-data && \  
groupmod -g 1000 www-data  
  
ADD php.ini /etc/php5/fpm/php.ini  
ADD php-cli.ini /etc/php5/cli/php.ini  
ADD www.conf /etc/php5/fpm/pool.d/www.conf  
ADD entrypoint.sh /entrypoint.sh  
ADD cron-entrypoint.sh /cron-entrypoint.sh  
  
RUN chmod u+x /entrypoint.sh && chmod u+x /cron-entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
EXPOSE 9000  

