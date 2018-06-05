FROM webdevops/php-apache:debian-9  
MAINTAINER Sohaib Afifi <me@sohaibafifi.com>  
  
# RUN echo "Acquire::http::proxy \"http://cache-adm.univ-artois.fr:8080/\"; "
> /etc/apt/apt.conf.d/99-proxy  
# ENV all_proxy "http://cache--adm.univ-artois.fr:8080"  
  
RUN /usr/local/bin/apt-install \  
nano \  
net-tools \  
php7.0-ldap \  
php7.0-dom \  
php7.0-mbstring \  
php-imap \  
php-pecl-http \  
mailutils \  
ssmtp \  
php7.0-pgsql \  
&& docker-image-cleanup  
  
COPY ./root /  
EXPOSE 80 443 9000  

