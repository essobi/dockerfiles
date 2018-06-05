FROM debian:stretch-slim  
  
# Environments for normal work of container  
ENV TWITCH_USER=MyBot  
ENV TWITCH_CHANNEL=#mychannel  
ENV TWITCH_TOKEN=oauth:xxxxxxx  
  
# Default environments for work with RabbitMQ  
ENV RABBIT_HOST=rabbitmq  
ENV RABBIT_PORT=5672  
ENV RABBIT_USER=guest  
ENV RABBIT_PASS=guest  
  
# RabbitMQ's queues for work  
ENV RABBIT_QUEUE_SOCIAL=social  
ENV RABBIT_QUEUE_CHAT=chat  
  
# List of dependencies  
ENV DEPS="php-bcmath php-mbstring php-mcrypt php-gettext php-curl php-cli php-
intl php-zip php-amqp composer git rsync"  
# Install dependecies and clean the cache  
RUN apt-get update \  
&& apt-get install -y ${DEPS} \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add php config  
ADD ["php.ini", "/etc/php/7.0/cli/php.ini"]  
  
# Add work files  
ADD ["composer.json", "/opt/"]  
ADD ["scripts/", "/opt/scripts/"]  
  
# Install all php deps  
RUN composer update --working-dir=/opt  
  
# Execute the php executer  
ENTRYPOINT ["/usr/bin/php", "-f"]  

