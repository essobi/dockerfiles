#  
# Php Dockerfile  
#  
# https://github.com/tamboraorg/docker/crephpdev  
#  
# Pull base image.  
FROM tamboraorg/crephp  
  
# Fixes some weird terminal issues such as broken clear / CTRL+L  
ENV TERM=linux  
  
  
# Install selected debug extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php-xdebug \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
# Install composer and selected extensions  
RUN apt-get update \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* ~/.composer  
  
WORKDIR "/var/www/cre"

