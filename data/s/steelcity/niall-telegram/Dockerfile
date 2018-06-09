FROM thruio/docker-webapp:latest  
ADD . /app  
  
# Add startup scripts  
RUN mkdir /etc/service/niall  
ADD docker/run.niall.sh /etc/service/niall/run  
RUN chmod +x /etc/service/*/run  
  
RUN composer install  
  
RUN rm /app/vendor/longman/telegram-bot/src/Commands/*.php

