FROM ubuntu:16.04  
LABEL description="Ubuntu Nginx PHP Stack inspired by Trellis" vendor="21st
digital" version="1.0"  
  
# Install locales  
RUN apt update && \  
apt install -y locales && \  
locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Get latest version of software-properties-common first  
RUN apt update && apt upgrade -y && apt install -y software-properties-common  
  
# Basic Requirements  
RUN apt update && \  
apt install -y curl unzip supervisor wget  
  
# Add PHP 7.2 PPA and install PHP 7.2  
RUN add-apt-repository -y ppa:ondrej/php && \  
apt update && \  
apt install -y php7.2-common php7.2-curl php7.2-dev php7.2-fpm php7.2-gd
php7.2-mbstring php7.2-mysql php7.2-opcache php7.2-tidy php7.2-xml
php7.2-xmlrpc php7.2-zip php-memcache php-memcached php-redis && \  
mv /etc/php/7.2/fpm/pool.d/www.conf /etc/php/7.2/fpm/pool.d/www.disabled  
  
# PHP configuration  
COPY php/php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf  
COPY php/wordpress.conf /etc/php/7.2/fpm/pool.d/wordpress.conf  
COPY php/wordpress.ini /etc/php/7.2/mods-available/wordpress.ini  
RUN ln -sf /etc/php/7.2/mods-available/wordpress.ini
/etc/php/7.2/fpm/conf.d/90-wordpress.ini  
  
# Install Xdebug  
RUN apt update && apt install -y php-xdebug  
  
# Xdebug configuration  
COPY xdebug/xdebug.ini /etc/php/7.2/mods-available/xdebug.ini  
  
# Add Nginx PPA & install Nginx  
RUN add-apt-repository -y ppa:nginx/development && \  
apt update && \  
apt install -y nginx && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Nginx configuration  
COPY nginx/h5bp-server-configs /etc/nginx/h5bp-server-configs  
COPY nginx/h5bp /etc/nginx/h5bp  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/wordpress-site.conf /etc/nginx/sites-available/default  
  
# Misc. Cleanup  
RUN mkdir /run/php && \  
apt remove -y --purge software-properties-common && \  
apt -y autoremove && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Supervisor configuration  
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]

