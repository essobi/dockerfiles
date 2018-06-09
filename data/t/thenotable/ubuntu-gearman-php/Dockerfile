FROM thenotable/ubuntu-gearman  
MAINTAINER Daniel Kennedy dkennedy4@gmail.com  
  
RUN apt-get update && apt-get install -y \  
php5 \  
php5-dev \  
php5-cli \  
php-pear  
  
ENV PHP_CLI_INI_FILE /etc/php5/cli/php.ini  
  
# Cli Logging  
RUN sed -i "s/;error_log = syslog/error_log = \/var\/log\/php_errors.log/g"
$PHP_CLI_INI_FILE  
RUN touch /var/log/php_errors.log  
RUN chown www-data: /var/log/php_errors.log  
RUN chmod +rw /var/log/php_errors.log  
  
# Install Gearman Pecl Extension  
RUN pecl install gearman  
RUN echo "extension=gearman.so" >> ${PHP_CLI_INI_FILE}

