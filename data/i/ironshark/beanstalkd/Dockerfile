FROM phusion/baseimage:latest  
MAINTAINER Daniel Korger <korger@ironshark.de>  
  
# install requirements  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && apt-get install -y \  
beanstalkd \  
git \  
php5-cli \  
supervisor  
ENV DEBIAN_FRONTEND text  
  
VOLUME ["/data"]  
  
# php composer  
WORKDIR /tmp  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# beanstalkd console  
WORKDIR /opt/beanstalk_console  
ADD composer.json /opt/beanstalk_console/composer.json  
RUN composer install  
WORKDIR /opt/beanstalk_console/vendor/ptrofimov/beanstalk_console  
RUN sed -i "s/'storage' =>.*/'storage' =>
'\/data\/beanstalk_console_storage.json',/" config.php  
  
WORKDIR /  
  
# clean up  
RUN apt-get clean \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8080  
EXPOSE 11300  
ADD sys/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

