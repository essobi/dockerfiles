FROM ubuntu:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="PHP-REDIS" \  
org.label-schema.description="LARP: Linux, Apache, Redis, PHP." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/php-redis" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --name=phpredis -p 8080:80 -h larp -d
jorgeandrada/php-redis"  
#instalamos paqueteria  
RUN apt-get update && \  
apt-get install -y unzip \  
apt-utils \  
curl \  
apache2 \  
libapache2-mod-php \  
libapache2-mod-php7.0 \  
php7.0 \  
php7.0-cli \  
php7.0-json \  
php-curl \  
jq \  
php-redis \  
redis-tools && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/archives/*  
  
  
#Personalizamos zona horaria y apache2  
RUN echo "Europe/Madrid" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
rm -rf /var/www/html/index.html  
COPY index.php /var/www/html/index.php  
  
#exponemos puertos  
#EXPOSE 80  
#directorio de trabajo por defecto  
WORKDIR /var/www/html  
  
#variables de entorno  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
#Ejecuto apache2 al inicio  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

