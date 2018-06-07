FROM nimmis/apache-php7  
  
MAINTAINER Jasper Roel <jasperroel@gmail.com>  
  
RUN groupadd -r jotihunt-site && useradd --no-log-init -r -g jotihunt-site
jotihunt-site  
  
## Setup apache  
COPY docker/jotihunt-vhost.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Make sure we can log apache  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
# Setup the site  
WORKDIR /var/www/jotihunt-site  
COPY . .  
  
COPY docker/docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

