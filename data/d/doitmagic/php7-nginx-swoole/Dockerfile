FROM ubuntu:trusty  
  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
python-software-properties \  
software-properties-common  
  
# add NGINX official stable repository  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/nginx.list  
  
# add PHP7 unofficial repository
(https://launchpad.net/~ondrej/+archive/ubuntu/php)  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/php.list  
  
RUN apt-add-repository -y ppa:mosquitto-dev/mosquitto-ppa  
  
# install packages  
RUN apt-get update && \  
apt-get -y --force-yes --no-install-recommends install \  
supervisor \  
curl \  
nginx \  
php7.1-fpm php7.1-dev php7.1-cli php7.1-common php7.1-curl php7.1-gd
php7.1-intl php7.1-json php7.1-mbstring php7.1-mcrypt php7.1-mysql
php7.1-opcache php7.1-soap php7.1-xml php7.1-xmlrpc php7.1-xsl php7.1-zip
php7.1-gd  
  
RUN apt-get update && \  
apt-get install -y --force-yes git wget libssl-dev zlib1g-dev libicu-dev g++
make cmake libuv-dev libgmp-dev uuid-dev libpcre3-dev php-pear php5-dev
mosquitto libmosquitto-dev && \  
apt-get autoclean -y --force-yes && \  
apt-get clean -y --force-yes  
  
# Install the composer  
RUN curl -sS http://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer  
RUN chmod +x /usr/bin/composer  
  
# configure NGINX as non-daemon  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# configure php-fpm as non-daemon  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf  
  
# clear apt cache and remove unnecessary packages  
RUN apt-get autoclean && apt-get -y autoremove  
  
# NGINX mountable directories for config and logs  
VOLUME ["/etc/nginx/sites-enabled","/etc/nginx/sites-available",
"/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]  
  
# copy config file for Supervisor  
COPY config/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
# backup default default config for NGINX  
RUN cp /etc/nginx/sites-available/default /etc/nginx/sites-
available/default.bak  
  
# copy local defualt config file for NGINX  
COPY config/nginx/default /etc/nginx/sites-available/default  
  
# php7.1-fpm will not start if this directory does not exist  
RUN mkdir /run/php  
  
RUN apt-get update && \  
apt-get install -f -y --force-yes libpcre3-dev php-pear php5-dev && \  
pecl install swoole && \  
pecl install hprose && \  
echo "extension=swoole.so" >> /etc/php/7.1/fpm/php.ini && \  
echo "extension=hprose.so" >> /etc/php/7.1/fpm/php.ini  
  
RUN echo 'extension=swoole.so' >> /etc/php/7.1/cli/php.ini  
RUN echo "extension=hprose.so" >> /etc/php/7.1/cli/php.ini  
  
RUN phpenmod swoole  
RUN phpenmod hprose  
  
RUN pecl install Mosquitto-alpha  
  
RUN echo "extension=mosquitto.so" >> /etc/php/7.1/cli/php.ini  
RUN echo "" > /etc/php/7.1/mods-available/Mosquitto-alpha.ini  
  
RUN phpenmod Mosquitto-alpha  
  
RUN apt-get update && \  
apt-get install -y --force-yes mosquitto mosquitto-clients python-mosquitto  
  
COPY config/mosquitto/mosquitto.conf /etc/mosquitto/mosquitto.conf  
  
# NGINX mountable directory for apps  
VOLUME ["/var/www"]  
  
WORKDIR /var/www  
  
# NGINX ports  
EXPOSE 80 443 8000 1883 1884  
CMD ["/usr/bin/supervisord"]  

