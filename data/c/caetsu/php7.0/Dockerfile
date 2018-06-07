FROM ubuntu:xenial  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Change sources to a server in Portugal to make package download faster  
RUN sed -i 's/http:\/\//http:\/\/pt./g' /etc/apt/sources.list  
  
# Update and upgrade system if necessary  
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade  
  
# PHP Installation  
RUN apt-get -y install php7.0 php7.0-fpm php7.0-xml php7.0-gd php7.0-json
php7.0-mbstring php7.0-soap php7.0-zip php7.0-opcache php7.0-curl php7.0-pgsql
php7.0-mysql php-xdebug php-redis php-imagick  
  
# Install Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& php composer-setup.php && mv composer.phar /usr/local/bin/composer && chmod
+x /usr/local/bin/composer  
  
# Overidden configuration files  
COPY conf /  
  
# Install Blackfire  
# It creates some configuration files for PHP  
RUN php -r
"readfile('https://blackfire.io/api/v1/releases/probe/php/linux/amd64/70');" >
/tmp/blackfire-probe.tar.gz && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp &&
mv /tmp/blackfire-*.so $(php -r "echo ini_get('extension_dir');")/blackfire.so
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
/etc/php/7.0/mods-available/blackfire.ini && phpenmod blackfire  
  
# Create a user to match the GUID of our user  
# TODO A better solution is required because machines may have multiple users  
RUN useradd application  
WORKDIR /opt/application  
  
EXPOSE 9000  
ENTRYPOINT ["php-fpm7.0", "--nodaemonize"]

