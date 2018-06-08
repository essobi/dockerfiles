#  
# Nasqueron - Notifications image  
#  
FROM nasqueron/nginx-php7-fpm:novolume  
MAINTAINER Nasqueron Organisation <docker@nasqueron.org>  
  
#  
# Prepare the container  
#  
COPY files /  
  
WORKDIR /var/wwwroot/default  
  
RUN git init && git remote add origin
https://github.com/nasqueron/notifications.git && \  
git fetch && git checkout -t origin/master && \  
composer install --ignore-platform-reqs --no-dev -o && \  
chown -R app:app /var/wwwroot/default  
  
#  
# Run the container  
#  
CMD ["/usr/local/sbin/init-container"]  

