FROM imiluzern/base-backend:latest  
  
RUN echo "* * * * * echo "Hello world" >> /var/log/cron.log 2>&1" | crontab -  
  
RUN touch /var/log/cron.log  
  
COPY ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir -p /var/log/supervisor  
  
COPY ./ /var/www/html  
  
RUN mv /var/www/html/.env.cloud.dev /var/www/html/.env  
  
RUN chmod -R 777 /var/www/html/bootstrap && chmod -R 777 /var/www/html/storage  
  
RUN wget https://getcomposer.org/download/1.2.0-RC/composer.phar  
  
VOLUME ["/var/www/html/vendor", "/var/www/html/node_modules",
"/var/www/html/public/bower_components", "/var/www/html/public/compiled"]  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]

