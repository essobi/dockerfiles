FROM ubuntu:16.04  
# Define default answers for debconf and set  
# debian frontend to noninteractive mode.  
COPY scripts/*.sh /scripts/  
RUN chmod +x /scripts/*  
RUN /scripts/defaults.sh  
RUN export DEBIAN_FRONTEND=noninteractive  
  
ADD https://deb.nodesource.com/setup_6.x /scripts/nodejs.sh  
RUN chmod +x /scripts/nodejs.sh && sync && /scripts/nodejs.sh  
RUN rm -f /scripts/nodejs.sh  
  
# Install packages  
RUN apt-get clean && apt-get -y update && apt-get install -y locales software-
properties-common \  
&& locale-gen en_US.UTF-8  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt -y update && apt install -y --no-install-recommends \  
git \  
nginx \  
php7.2 \  
php7.2-gd \  
php7.2-curl \  
php7.2-fpm \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-tidy \  
php7.2-zip \  
php7.2-xml \  
php7.2-redis \  
php-soap \  
mysql-client-5.7 \  
composer \  
nodejs \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* && echo 'Packages installed and lists cleaned'  
  
# Add configuration files  
COPY conf/php/* /etc/php/7.2/fpm/conf.d  
COPY conf/nginx/conf.d/* /etc/nginx/conf.d  
COPY conf/nginx/sites/* /etc/nginx/sites-enabled  
COPY conf/nginx/sites/* /etc/nginx/sites-available  
COPY conf/supervisor/* /etc/supervisor/conf.d/  
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Disable default site on nginx  
RUN rm -rf /etc/nginx/sites-enabled/default  
  
# Disable daemon mode on php-fpm  
RUN sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php/7.2/fpm/php-fpm.conf  
  
# Create run directories for mysql and php-fpm  
RUN mkdir /var/run/php  
  
# Expose HTTP port  
EXPOSE 80  
WORKDIR /var/www  
  
CMD ["/scripts/run.sh"]  
  

