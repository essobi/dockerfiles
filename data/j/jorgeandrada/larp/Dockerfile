FROM ubuntu:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="LARP" \  
org.label-schema.description="LARP: Linux, Apache, Redis, PHP." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/LARP" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --name=larp -p 8080:80 -h larp -d
jorgeandrada/larp"  
  
RUN apt-get update && \  
apt-get install -y unzip \  
apt-utils \  
curl \  
cron \  
apache2 \  
libapache2-mod-php \  
libapache2-mod-php7.0 \  
php7.0 \  
php7.0-cli \  
php7.0-json \  
php-curl \  
jq \  
php-redis \  
supervisor \  
wget \  
gcc \  
libc6-dev \  
make \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/archives/*  
  
#instalo la última versión de redis  
RUN cd /tmp && \  
wget http://download.redis.io/releases/redis-3.2.4.tar.gz && \  
tar -xzf redis-3.2.4.tar.gz && \  
make -C /tmp/redis-3.2.4/ && \  
make -C /tmp/redis-3.2.4/ install && \  
rm -rf /tmp/*  
  
#Personalizamos apache2  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN rm -rf /var/www/html/index.html  
COPY index.php /var/www/html/index.php  
  
#Personalizamos redis  
COPY redis.conf /etc/redis/  
RUN chown root:root /etc/redis/redis.conf && \  
chmod 644 /etc/redis/redis.conf && \  
mkdir -p /var/lib/redis  
  
#exponemos puertos  
EXPOSE 6379  
EXPOSE 80  
#directorio de trabajo por defecto  
WORKDIR /var/www/html  
  
# #Ejecuto el supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN chown root:root /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

