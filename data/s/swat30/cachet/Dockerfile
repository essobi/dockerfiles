FROM cachethq/docker:base-d3506c1  
  
RUN cd /var/www/html && \  
git init && \  
git remote add origin https://github.com/CloudA/Cachet.git && \  
git fetch && \  
git checkout -t origin/clouda && \  
rm -Rf .git && \  
chown -R www-data /var/www/html && \  
php composer.phar install --no-dev -o && \  
cp -n vendor/jenssegers/date/src/Lang/zh.php
vendor/jenssegers/date/src/Lang/zh-CN.php  
  
COPY docker/entrypoint.sh /sbin/entrypoint.sh  
  
WORKDIR /var/www/html/  
  
# copy the various nginx and supervisor conf (to handle both fpm and nginx)  
COPY docker/.env.docker /var/www/html/.env  
  
COPY docker/crontab /etc/cron.d/artisan-schedule  
RUN chmod 0644 /etc/cron.d/artisan-schedule &&\  
touch /var/log/cron.log  
  
EXPOSE 8000  
CMD ["/sbin/entrypoint.sh"]  

