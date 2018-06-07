FROM phusion/baseimage:latest  
  
LABEL maintainer "Doitmagic <razvan@doitmagic.com>"  
  
# add NGINX official stable repository  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/nginx.list && \  
# add PHP7 unofficial repository
(https://launchpad.net/~ondrej/+archive/ubuntu/php)  
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs` main" >
/etc/apt/sources.list.d/php.list && \  
# install packages  
apt-get update && \  
apt-get -y --force-yes --no-install-recommends install \  
supervisor \  
curl \  
nginx \  
zip \  
unzip \  
php7.1-fpm php7.1-dev php7.1-cli php7.1-common php7.1-curl php7.1-gd
php7.1-intl php7.1-json php7.1-mbstring php7.1-mcrypt php7.1-mysql
php7.1-opcache php7.1-soap php7.1-xml php7.1-xmlrpc php7.1-xsl php7.1-zip
php7.1-gd \  
git wget openssl libssl-dev zlib1g-dev libicu-dev g++ make cmake libuv-dev
libgmp-dev uuid-dev libpcre3-dev php-pear  
  
# clear apt cache and remove unnecessary packages  
RUN mkdir -p /etc/nginx/htpasswd/ \  
mkdir -p /etc/nginx/ssl && \  
# php7.1-fpm will not start if this directory does not exist  
mkdir /run/php && \  
echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null && \  
# Install the composer  
curl -sS http://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer && \  
chmod +x /usr/bin/composer && \  
# configure NGINX as non-daemon  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
COPY config/php/php.ini /etc/php/7.1/fpm/php.ini && \  
# configure php-fpm as non-daemon  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf && \  
# clear apt cache and remove unnecessary packages  
apt-get autoclean && apt-get -y autoremove && \  
# backup default default config for NGINX  
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
&& \  
apt-get autoclean -y --force-yes && \  
apt-get clean -y --force-yes  
  
# copy config file for Supervisor  
COPY config/supervisord/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
# NGINX mountable directory for apps, mountable directories for config and
logs  
VOLUME ["/var/www","/etc/nginx/sites-available", "/etc/nginx/ssl",
"/var/log/nginx"]  
  
WORKDIR /var/www  
  
# NGINX ports  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord"]  

