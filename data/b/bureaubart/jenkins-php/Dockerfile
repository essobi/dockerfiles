FROM jenkins  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
ant \  
php5-cli php5-sqlite php5-curl php5-gd php5-xdebug php-codecoverage \  
phpunit phploc php-codesniffer pdepend phpmd phpcpd phpdox \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -O /usr/local/bin/composer https://getcomposer.org/composer.phar &&
chmod +x /usr/local/bin/composer  
  
RUN echo "xdebug.max_nesting_level = 200" >> /etc/php5/mods-
available/xdebug.ini  
  
USER jenkins  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  

