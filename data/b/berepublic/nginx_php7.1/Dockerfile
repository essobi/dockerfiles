FROM berepublic/ubuntubaseimage  
  
MAINTAINER berepublic  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_DISABLE_XDEBUG_WARN 1  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
# Upgrade the container  
RUN apt-get clean && \  
apt-get update && \  
apt-get upgrade -y  
  
# Nginx-PHP Installation  
RUN apt-get install -y nano unzip build-essential python-software-properties  
RUN add-apt-repository -y ppa:ondrej/php  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
# Install php  
RUN apt-get install -y php7.1 php7.1-common php7.1-cli php7.1-fpm  
  
# Install extension php  
RUN apt-get install -y php7.1-mysql php7.1-curl php7.1-gd php7.1-intl
php7.1-mcrypt php7.1-json php7.1-xml php7.1-mbstring  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.1/cli/php.ini  
  
# Install nginx  
RUN apt-get install -y nginx  
  
# Install memcached  
RUN apt-get install -y php7.1-memcached memcached  
  
# Cleanup  
RUN apt-get remove --purge -y python-software-properties && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.1/fpm/php.ini  
  
RUN mkdir /log  
RUN mkdir -p /var/www  
ADD default /etc/nginx/sites-available/default  
RUN mkdir /etc/service/nginx  
ADD nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
RUN mkdir /etc/service/phpfpm  
ADD phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
RUN mkdir /etc/service/memcached  
ADD memcached.sh /etc/service/memcached/run  
RUN chmod +x /etc/service/memcached/run  
  
RUN service php7.1-fpm start  
  
# Expose ports  
EXPOSE 80  
EXPOSE 443  
# End Nginx-PHP  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add path the phpunit (project level)  
ENV PATH /var/www/vendor/bin:$PATH  
  
# Set working dir  
WORKDIR /var/www  

