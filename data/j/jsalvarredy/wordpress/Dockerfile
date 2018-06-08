FROM php:5.6-apache  
MAINTAINER Joaquin Salvarredy <joaquin@salvarredy.com.ar>  
ENV DEBIAN_FRONTEND noninteractive  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y locales libapache2-mod-rpaf \  
libpng12-dev libjpeg-dev postfix mailutils rsyslog libcurl3 \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install mysql  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
# Configure timezone and locale  
RUN echo "America/Argentina/Buenos_Aires" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
RUN echo 'es_AR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN echo 'es_ES.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
RUN export LANGUAGE=es_ES.UTF-8 && \  
export LANG=es_ES.UTF-8 && \  
export LC_ALL=es_ES.UTF-8 && \  
locale-gen es_ES.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
RUN apt-get remove -y curl && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN printf "date.timezone=America/Argentina/Buenos_Aires\n" >>
/usr/local/etc/php/php.ini  
#Se pasa el access.log a archivo  
RUN sed -i 's|/proc/self/fd/1|/var/log/apache2/access.log|'
/etc/apache2/apache2.conf  
#Se pasa el error.log a stdout, para que salga en el log de docker  
RUN sed -i 's|/proc/self/fd/2|/proc/self/fd/1|' /etc/apache2/apache2.conf  
  
EXPOSE 80  
RUN a2enmod rewrite  
COPY start.sh /start.sh  
CMD ["/start.sh"]  
  

