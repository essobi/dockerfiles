FROM sumpfgottheit/centos7  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
# Install httpd, php aund php-pgsql  
RUN yum -y install httpd php php-pgsql  
RUN yum -y clean all  
RUN rm /etc/httpd/conf.d/userdir.conf  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && mv /usr/local/bin/composer.phar /usr/local/bin/composer  
RUN mkdir -p /usr/local/share/php  
WORKDIR /usr/local/share/php  
RUN composer require monolog/monolog  
WORKDIR /  
RUN echo 'include_path =
".:/usr/share/pear:/usr/share/php:/usr/local/share/php"' >> /etc/php.ini  
  
EXPOSE 80 443  
ADD apache-foreground.sh /apache-foreground.sh  
ADD configure-apache.sh /configure-apache.sh  
RUN /configure-apache.sh  
  
ADD logstash.conf /etc/logstash.conf  
ADD logstash.pattern /etc/logstash.pattern  
  
CMD /apache-foreground.sh  
  
VOLUME ["/logs", "/var/www/html"]  
  

