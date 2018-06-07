FROM phusion/baseimage:0.9.19  
  
MAINTAINER Meillaud Jean-Christophe (jc@houseofagile.com)  
  
ENV HOME /root  
  
# PHP >7  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 4F4EA0AAE5267A6C
&& \  
LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php && \  
apt-get update && apt-get install -y python-software-properties && \  
apt-get update && apt-get install -y \  
nginx \  
software-properties-common \  
git-core \  
php7.0 \  
php7.0-fpm \  
php7.0-mysql \  
php7.0-imagick \  
php7.0-imap \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-cli \  
php7.0-gd \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-common \  
php-pear \  
curl \  
php7.0-json \  
php7.0-intl \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-zip \  
php-apcu \  
python \  
g++ \  
make && \  
chown www-data -R /usr/share/nginx/ && \  
echo "source ~/.bashrc">>/root/.bash_profile && \  
curl -sSL https://raw.github.com/beaudev/bash-profile/master/install-bash-
profile.sh|bash && \  
apt-get clean && rm -rf /tmp/* /var/tmp/* && \  
service php7.0-fpm start  
  
# generate a simple index file with phpinfo  
ADD nginx-default.conf /etc/nginx/sites-available/default  
RUN sed -i 's#%%php_fpm_sock_file%%#/run/php/php7.0-fpm.sock#g'
/etc/nginx/sites-available/default && \  
echo "<?php\nphpinfo();">/var/www/html/index.php  
  
# nginx and php-fpm7.0 service  
RUN mkdir /etc/service/01_phpfpm /etc/service/02_nginx  
ADD build/php7.0-fpm.sh /etc/service/01_phpfpm/run  
ADD build/nginx.sh /etc/service/02_nginx/run  
RUN chmod +x /etc/service/01_phpfpm/run /etc/service/02_nginx/run  
  
  
EXPOSE 80  
  
CMD ["/sbin/my_init"]  

