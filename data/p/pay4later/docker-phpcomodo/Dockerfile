FROM pay4later/docker-comodo:latest  
MAINTAINER Andrew Mackrodt <andrew.mackrodt@pay4later.com>  
  
# install packages  
RUN apt-get -q -y update && \  
apt-get -q -y install git libapache2-mod-php5 php5-curl php5-apcu && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/*  
  
# clone the phpwkhtmltopdf-server project  
RUN git clone \--depth 1 --branch v0.1.0a https://github.com/pay4later/comodo-
server.git /opt/comodo-server && \  
rm -rf /var/www/html/ && \  
ln -s /opt/comodo-server/public/ /var/www/html && \  
cd /opt/comodo-server/ && \  
rm -rf .git/ && \  
php -r "readfile('https://getcomposer.org/installer');" | php && \  
php composer.phar install --no-interaction --no-dev --prefer-dist && \  
php composer.phar generate-hydrators && \  
rm -f composer.phar  
  
EXPOSE 80  
ENTRYPOINT ["apache2ctl"]  
  
CMD ["-D FOREGROUND"]  

