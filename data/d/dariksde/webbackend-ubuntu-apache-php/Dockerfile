FROM dariksde/webbackend-ubuntu-apache2:latest  
  
MAINTAINER Daniel Rippen <rippendaniel@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y software-properties-common python-software-properties
&& \  
export LANG=C.UTF-8 && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y \  
php7.1 \  
php7.1-cli \  
php7.1-fpm \  
libapache2-mod-php7.1 \  
libapache2-mod-rpaf \  
php7.1-gd \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-intl \  
php7.1-sqlite3 \  
php7.1-xml \  
php7.1-zip \  
php7.1-curl \  
php7.1-opcache \  
php7.1-readline \  
php7.1-soap \  
sendmail \  
sendmail-bin \  
mailutils && \  
apt-get clean && \  
mkdir -p /run/php  
  
RUN rm -rf /var/lib/apt/lists/* && \  
a2dismod php7.1 mpm_prefork ssl && \  
a2enmod actions alias proxy_fcgi mpm_event setenvif dav dav_fs rpaf rewrite &&
\  
a2enconf php7.1-fpm  
  
COPY ./*.sh /usr/local/bin/  
COPY ./php_mail.ini /usr/local/etc/php/conf.d/mail.ini  
RUN chmod a+x /usr/local/bin/*.sh  
  
ADD ports.conf /etc/apache2/ports.conf  
ADD start.sh /start.sh  
  
RUN sed -i -e "s/^upload_max_filesize\s*=\s*2M/upload_max_filesize = 200M/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/^post_max_size\s*=\s*8M/post_max_size = 200M/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/^output_buffering\s*=\s*4096/output_buffering = 0/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/^max_execution_time\s*=\s*30/max_execution_time = 5000/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/^max_input_time\s*=\s*60/max_input_time = 2000/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i -e "s/^max_input_time\s*=\s*60/max_input_time = 2000/"
/etc/php/7.1/fpm/php.ini  
RUN echo srv-06.server.rippen-ks.de > /etc/mail/local-host-names  
  
CMD ["/bin/bash", "/start.sh"]  

