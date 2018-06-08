FROM ubuntu:17.10  
# packages to run and serve symfony code  
RUN apt-get update && apt-get install -y \  
zip \  
unzip \  
php7.1 \  
php7.1-fpm \  
php7.1-mysql \  
php7.1-sqlite \  
php7.1-pgsql \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-curl \  
php7.1-zip \  
php7.1-imagick \  
php7.1-gd \  
php7.1-xdebug \  
nginx  
# useful stuff to work on the container  
RUN apt-get update && apt-get install -y sudo \  
htop \  
vim \  
iputils-ping \  
net-tools \  
mysql-client \  
sqlite3 \  
postgresql-client \  
mc  
# create a user with a home and a sudo privilege  
# pwd and username is also 'developer'  
RUN useradd -mUG sudo developer && \  
echo 'developer:developer' | chpasswd && \  
chsh -s /bin/bash developer  
# run php-fpm and nginx services as 'developer' user  
RUN sed -i -- 's/www-data/developer/g' /etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -- 's/www-data/developer/g' /etc/nginx/nginx.conf  
# add site configs for nginx (one for dev and one for prod mode)  
COPY nginx/* /etc/nginx/sites-enabled/  
COPY php/xdebug.ini /etc/php/7.1/mods-available/xdebug.ini  
# copy the shell script which will start the nginx and php-fpm services  
COPY entrypoint.sh /home/developer/  
# start services ; this script should never return  
CMD /home/developer/entrypoint.sh ; sleep infinity

