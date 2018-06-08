FROM webdevops/php-apache:debian-8-php7  
RUN wget -qO- https://get.docker.com/ | sh  
COPY ./src /app  
RUN mkdir -p /app/var/dev && chown -R application:application /app/var &&
chmod -R 777 /app/var  
RUN cd /app && composer install  
RUN gpasswd -a application docker

