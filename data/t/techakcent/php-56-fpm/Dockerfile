FROM danieldent/php-56-fpm  
  
# Download WordPress CLI  
RUN curl -L "https://github.com/wp-cli/wp-cli/releases/download/v0.24.1/wp-
cli-0.24.1.phar" > /usr/bin/wp && \  
chmod +x /usr/bin/wp  
#add cron  
RUN apt-get update && apt-get install -y cron \  
vim  
RUN touch /var/log/cron.log  
COPY hello-cron /etc/cron.d/hello-cron  
RUN crontab /etc/cron.d/hello-cron  
COPY /entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

