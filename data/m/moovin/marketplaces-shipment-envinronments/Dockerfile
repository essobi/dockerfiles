#FROM ubuntu:14.04  
FROM ubuntu:15.10  
MAINTAINER Moovin Plataforma <cadastro@moovin.com.br>  
ENV DEBIAN_FRONTEND noninteractive  
  
EXPOSE 80  
##########################################  
### INSTALL GIT AND BASIC DEPENDENCIES ###  
##########################################  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
wget \  
debconf-utils \  
g++ \  
libssl-dev \  
unzip  
  
RUN apt-get install -y --no-install-recommends software-properties-common
build-essential  
  
#####################  
### INSTALL PHP 7 ###  
#####################  
# ADD REPOSITORY FOR PHP 7  
RUN add-apt-repository ppa:ondrej/php -y  
  
RUN apt-get update && apt-get install -y --force-yes \  
php7.0-cli \  
php7.0-fpm \  
libapache2-mod-php7.0 \  
php7.0-cgi \  
php7.0 \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-curl  
  
COPY configs/php/fpm-pool-www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
######################  
## INSTALL COMPOSER ##  
######################  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
#####################  
### INSTALL NGINX ###  
#####################  
RUN apt-get install nginx -y  
  
# NGINX configs; no need for virtual hosting  
COPY configs/nginx/default /etc/nginx/nginx.conf  
  
#########################  
### SSH CONFIGURATION ###  
#########################  
# Create dir or ignore if exists  
RUN mkdir -p ~/.ssh  
  
# Create empty known_hosts  
RUN touch /root/.ssh/known_hosts  
  
# Add bitbucket's ssh fingerprint to the list of known hosts  
RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts  
  
# Copy the private key of the repository  
ADD configs/ssh/alderaan /root/.ssh/id_rsa  
  
# Change permissions of key to avoid unauthorized read  
RUN chmod 600 /root/.ssh/id_rsa  
  
WORKDIR /var/www  
RUN rm -r html  
RUN git clone git@bitbucket.org:moovin/marketplaces-shipment.git .  
  
RUN chmod 755 -R /var/www  
RUN chmod -R o+w /var/www/storage  
RUN chown www-data:www-data -R /var/www/storage  
RUN chown www-data:www-data -R /var/www/bootstrap/cache  
  
RUN composer install  
  
# Copy the startup script and add execution permission  
COPY startup.sh /usr/bin/startup  
RUN chmod +x /usr/bin/startup  
  
# Enable startup on run  
CMD /usr/bin/startup  

