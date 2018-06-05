FROM debian:stable  
  
RUN useradd -mUG sudo app \  
&& echo 'app:app' | chpasswd \  
&& chsh -s /bin/bash app \  
&& mkdir /home/app/docroot  
  
RUN apt-get update \  
&& apt-get -y install \  
apt-transport-https \  
gnupg \  
curl \  
lsb-release \  
ca-certificates \  
&& curl https://packages.sury.org/php/apt.gpg | apt-key add - \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
COPY ./nginx/server.conf /etc/nginx/conf.d/server.conf  
COPY ./entrypoint.sh /init.sh  
RUN apt-get update \  
&& apt-get -y install \  
php7.2 \  
php7.2-fpm \  
php7.2-curl \  
php7.2-zip \  
nginx \  
git \  
gcc \  
g++ \  
make \  
&& mkdir /var/app \  
&& mkdir /var/app/resources  
  
RUN cd /var/app/resources && git clone
https://github.com/michaelrsweet/htmldoc.git \  
&& cd htmldoc \  
&& ./configure \  
&& make \  
&& make install  
  
COPY ./resources/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
/var/app/resources/  
RUN cd /var/app/resources && tar xf wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz \  
&& apt-get update && apt-get -y install \  
libfontconfig1 \  
libxrender1 \  
fontconfig \  
&& cp wkhtmltox/bin/wkhtmlto* /usr/local/bin/  
  
  
RUN sed -i -- 's/listen[[:space:]]*=[[:space:]]*.*/listen = 0.0.0.0:8080/g'
/etc/php/7.2/fpm/pool.d/www.conf \  
&& sed -i -- 's/www-data/app/g' /etc/php/7.2/fpm/pool.d/www.conf \  
&& sed -i -- 's/www-data/app/g' /etc/nginx/nginx.conf \  
&& mkdir /var/app/docroot  
  
COPY ./application/ /var/app/docroot/  
  
ENTRYPOINT ["/init.sh"]

