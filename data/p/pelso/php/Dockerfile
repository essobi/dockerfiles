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
  
RUN apt-get update \  
&& apt-get -y install \  
zip \  
unzip \  
php5.6 \  
php5.6-fpm \  
php5.6-mysql \  
php5.6-sqlite \  
php5.6-pgsql \  
php5.6-xml \  
php5.6-mbstring \  
php5.6-curl \  
php5.6-zip \  
php5.6-intl \  
php5.6-imagick \  
php5.6-gd  
  
RUN sed -i -- 's/www-data/app/g' /etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i -- 's/listen[[:space:]]*=[[:space:]]*.*/listen = 0.0.0.0:8080/g'
/etc/php/5.6/fpm/pool.d/www.conf  
  
CMD service php5.6-fpm start \  
&& service php5.6-fpm restart \  
&& sleep infinity  

