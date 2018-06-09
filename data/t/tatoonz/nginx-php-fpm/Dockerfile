FROM ubuntu:wily  
  
MAINTAINER TaToonz (peerapath.t@gmail.com)  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
ca-certificates \  
curl \  
gettext-base \  
git \  
nginx \  
php5-curl\  
php5-fpm \  
php5-mcrypt \  
ssh \  
supervisor \  
&& php5enmod mcrypt \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
# change server timezone  
RUN rm -rf /etc/localtime \  
&& ln -sn /usr/share/zoneinfo/Asia/Bangkok /etc/localtime  
  
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY conf/nginx/default.conf /etc/nginx/sites-available/default  
  
COPY conf/php-fpm/timezone.ini /etc/php5/fpm/conf.d/timezone.ini  
COPY conf/php-fpm/docker.conf /etc/php5/fpm/pool.d/z-docker.conf  
  
COPY conf/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
WORKDIR /usr/share/nginx/html  
  
COPY ./src ./  
  
EXPOSE 80 443 9000  
CMD ["/usr/bin/supervisord"]

