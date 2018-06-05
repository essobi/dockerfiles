FROM meupatrocinio/docker-php7-newrelic:latest  
  
# Repository/Image Maintainer  
MAINTAINER Rafael Bernardo <rafael@meupatrocinio.com>  
  
# Reset user to root to allow software install  
USER root  
  
RUN echo "* * * * * php /var/www/app/artisan schedule:run >> /var/log/cron
2>&1" >> /etc/crontabs/root  
RUN sed -i '/bash/a crond' /scripts/start.sh  
RUN touch /var/log/cron  
# Define the entry point that tries to enable newrelic  
ENTRYPOINT ["/tini", "--", "/scripts/start.sh"]  
CMD ["tail", "-f", "/var/log/cron"]

