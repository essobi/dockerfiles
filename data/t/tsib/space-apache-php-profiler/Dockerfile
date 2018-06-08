FROM tutum/apache-php  
RUN usermod -u 33 www-data  
RUN apt-get update  
RUN apt-get install -y php5-xdebug  
RUN apt-get install -y sendmail  
RUN apt-get install -y vim  
RUN a2enmod expires && \  
a2enmod headers && \  
php5enmod mcrypt  
RUN apt-get install -y php5-imagick  
  
# Installing Blackfire profiler  
RUN apt-get install -y php5-mysql  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\nblackfire.log_level=4\n"
> /etc/php5/apache2/conf.d/blackfire.ini  
  
RUN service apache2 restart  
ADD hosts.sh /home/hosts.sh  

