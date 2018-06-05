FROM maxexcloo/nginx-php  
  
# Adding backports for nodejs  
RUN echo "# Backports repository\ndeb http://http.debian.net/debian wheezy-
backports main contrib non-free" >> /etc/apt/sources.list  
  
# Installing additional dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy install nodejs git curl
php5-intl  
RUN apt-get -qy clean  
  
# Installing composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Installing orocrm  
RUN mkdir -p /var/www/orocrm/ && \  
git clone \--depth 1 --branch 1.8.2 https://github.com/orocrm/crm-
application.git /var/www/orocrm && \  
ln -s /var/www/orocrm /var/www/orocrm.local  
RUN cd /var/www/orocrm && \  
composer install --no-dev --prefer-dist  
RUN chown core:core -R /var/www/  
  
# Adding required configuration for nginx, php and orocrm  
ADD nginx-orocrm.conf /etc/nginx/host.d/  
ADD php-config.conf /data/config/  
ADD php-cli.ini /etc/php5/cli/conf.d/30-orocrm.ini  
ADD parameters.yml /var/www/orocrm/app/config/  
RUN chown core:core /var/www/orocrm/app/config/parameters.yml  
  
# Patching orocrm to support docker's filesystem  
ADD orocrm-patch-filesystem.patch /root/  
RUN cd /var/www/orocrm/app/ && \  
patch < /root/orocrm-patch-filesystem.patch  

