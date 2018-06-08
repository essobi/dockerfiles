########################################  
# Dockerfile to build NGINX HHVM image  
########################################  
# Base image  
FROM nginx:latest  
  
# Author: MobileSnapp Inc.  
MAINTAINER MobileSnapp <support@mobilesnapp.com>  
  
# Add HHVM repo  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 && \  
echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
  
# Install supervisor, HHVM & tools  
RUN apt-get update && apt-get install -my \  
supervisor \  
hhvm \  
git \  
wget \  
curl \  
sqlite3 \  
libsqlite3-dev \  
&& apt-get clean  
  
# Install tools  
RUN cd $HOME && \  
wget http://getcomposer.org/composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
# Configuration  
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY ./config/php.ini /etc/hhvm/php.ini  
COPY ./config/nginx.conf /etc/nginx/nginx.conf  
COPY ./config/config.conf /etc/nginx/conf.d/config.conf  
COPY ./config/default /etc/nginx/sites-enabled/default  
COPY ./config/.bashrc /root/.bashrc  
  
# Copy source  
COPY index.php /var/www/site/index.php  
  
# Expose web and SSL ports.  
EXPOSE 80  
EXPOSE 443  
  
CMD ["/usr/bin/supervisord"]

