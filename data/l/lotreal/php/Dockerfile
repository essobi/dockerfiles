FROM eboraas/laravel:latest  
  
RUN apt update && apt install -y librdkafka-dev php-dev  
RUN pecl install rdkafka && echo extension=rdkafka.so >
/etc/php/7.0/cli/conf.d/20-kafka.ini  

