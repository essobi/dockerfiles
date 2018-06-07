FROM php:cli  
  
#RUN sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ Europe\/Moscow/g'
/etc/php/php.ini  
#RUN apk add php-openssl \  
# && apk add php-phar \  
# && apk add php-ctype \  
# && apk add git \  
# && apk add curl \  
# && curl -sS https://getcomposer.org/installer | php \  
# && mv composer.phar /usr/local/bin/composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN apt update \  
&& apt install -y zip \  
&& apt install -y git \  
&& apt install -y inotify-tools  
  
COPY composer.sh /tmp/composer.sh  
  
ENTRYPOINT ["/bin/bash", "-c"]  
  
CMD ["/tmp/composer.sh"]  
  

