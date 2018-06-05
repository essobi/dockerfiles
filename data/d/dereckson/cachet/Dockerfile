#  
# Nasqueron - Cachet image  
#  
FROM nasqueron/nginx-php-fpm:novolume  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
#  
# Prepare the container  
#  
COPY files /  
  
WORKDIR /var/wwwroot/default  
  
RUN git init && git remote add origin https://github.com/cachethq/Cachet.git
&& \  
git fetch && git checkout -t origin/master && \  
composer install --no-dev -o && \  
chown -R app:app /var/wwwroot/default  
  
#  
# Run the container  
#  
CMD ["/usr/local/sbin/init-container"]  
  

