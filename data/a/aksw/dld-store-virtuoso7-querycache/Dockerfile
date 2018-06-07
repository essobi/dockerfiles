FROM ubuntu:14.04  
MAINTAINER Konrad Abicht <abicht@informatik.uni-leipzig.de>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# update package index  
RUN apt-get update  
  
# install some basic packages  
# install the nginx server with PHP  
RUN apt-get install -y \  
git make curl nginx-light wget memcached redland-utils \  
php5 php5-fpm php5-common php5-cli php5-odbc php5-curl php5-memcached
php5-librdf \  
unixodbc  
  
# Add virtuoso odbc dependency to be able to connecto to virtuoso  
ADD libvirtodbc0_7.2_amd64.deb /  
RUN dpkg -i libvirtodbc0_7.2_amd64.deb  
RUN ln -s /etc/php5/mods-available/redland.ini
/etc/php5/cli/conf.d/20-redland.ini  
  
RUN rm -rf /var/www/*  
  
# Install composer  
RUN bash -c "wget http://getcomposer.org/composer.phar && mv composer.phar
/usr/local/bin/composer"  
  
RUN chmod +x /usr/local/bin/composer  
  
# Install Saft and dependencies  
ADD composer.json /var/www/composer.json  
WORKDIR /var/www  
RUN composer update  
  
ADD index.php /var/www/index.php  
  
# configure site for nginx  
ADD ontowiki-nginx.conf /etc/nginx/sites-available/  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /etc/nginx/sites-available/ontowiki-nginx.conf /etc/nginx/sites-
enabled/  
  
# configure odbc for virtuoso  
ADD odbc.ini /etc/  
  
# Add startscript and start  
ADD start.sh /start.sh  
  
VOLUME /var/www/logs  
  
CMD ["/bin/bash", "/start.sh"]  
  
# expose the HTTP port to the outer world  
EXPOSE 80  

