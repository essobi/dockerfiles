FROM profideo/php56-apache-node  
  
MAINTAINER Alban Duval <aduval@profideo.com>  
  
# update apt  
RUN apt-get update  
  
# Install imagemagick  
RUN apt-get install -y libmagickwand-dev  
RUN pecl install imagick  
RUN /usr/local/bin/docker-php-ext-enable imagick  
  
# NPM  
RUN chown profideo:profideo /home/profideo/.npm  
RUN npm cache clear && npm update -g && npm cache clean -f && npm install -g n
&& n 6.11.0  
RUN npm cache clear  
  
# PHP configuration  
COPY files/php.ini /usr/local/etc/php/php.ini  
  
# Supervisor  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

