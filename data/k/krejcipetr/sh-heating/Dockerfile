FROM php:5.4-cli  
COPY . /usr/src/sh-heating  
RUN docker-php-ext-install sysvsem \  
&& apt-get update && apt-get install -y tcl-dev expect-dev tcl-expect-dev\  
&& pecl install expect \  
&& docker-php-ext-enable expect  
WORKDIR /usr/src/sh-heating  
VOLUME /usr/src/sh-heating/logs  
#VOLUME /var/lib/sh-heating  
#VOLUME /usr/src/sh-heating/logs  
CMD php ./daemon/heating_control.php  

