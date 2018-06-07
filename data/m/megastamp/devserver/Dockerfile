FROM debian:stretch  
MAINTAINER Jonathan Grimmtjärn <stamp@stamp.se>  
  
ENV QUEUE_CONNECTION=redis  
ENV QUEUE_NAME=default  
  
RUN apt-get update -yqq && apt-get install -yyqq \  
git \  
openssh-client \  
php-imagick \  
php7.0-fpm \  
php7.0-bcmath \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-xml \  
php7.0-zip \  
php7.0-xdebug \  
supervisor \  
nginx \  
curl  
  
# Download trusted certs  
RUN mkdir -p /etc/ssl/certs && update-ca-certificates  
RUN mkdir -p /var/log/supervisord/apps  
RUN mkdir -p /run/php && touch /run/php/php7.0-fpm.sock && touch
/run/php/php7.0-fpm.pid  
  
# Install composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \  
mv composer.phar /usr/bin/composer && \  
chmod +x /usr/bin/composer  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Setup mailhog  
RUN curl -Lsf 'https://storage.googleapis.com/golang/go1.8.3.linux-
amd64.tar.gz' | tar -C '/usr/local' -xvzf -  
ENV PATH /usr/local/go/bin:$PATH  
RUN go get github.com/mailhog/mhsendmail  
RUN cp /root/go/bin/mhsendmail /usr/bin/mhsendmail  
RUN echo 'sendmail_path = "/usr/bin/mhsendmail --smtp-addr=mailhog:1025"' >
/etc/php/7.0/fpm/conf.d/30-mailhog.ini  
RUN echo 'sendmail_path = "/usr/bin/mhsendmail --smtp-addr=mailhog:1025"' >
/etc/php/7.0/cli/conf.d/30-mailhog.ini  
  
WORKDIR /var/www  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 80  

