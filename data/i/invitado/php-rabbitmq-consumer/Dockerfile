FROM php:7.2-alpine  
  
# Install needed PHP extensions.  
RUN docker-php-ext-install pdo_mysql sockets opcache bcmath  
  
# Install AMQP extension.  
RUN apk add --no-cache rabbitmq-c rabbitmq-c-dev $PHPIZE_DEPS \  
&& pecl install amqp-1.9.3 \  
&& docker-php-ext-enable amqp \  
&& apk del $PHPIZE_DEPS  
  
# Install rabbitmq-cli-consumer.  
RUN apk add --update rabbitmq-c-utils  
  
# Install dumb init.  
RUN apk add --update dumb-init && rm -rf /var/cache/apk/*  
  
# Add entrypoint script.  
COPY ./run.sh /opt/run.sh  
RUN chmod +x /opt/run.sh  
  
# Add entrypoint script.  
COPY ./entrypoint.sh /opt/entrypoint.sh  
RUN chmod +x /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/dev/true"]  

