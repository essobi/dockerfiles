FROM galeone/archlinux-updated-aur  
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>  
  
USER aur  
RUN pacaur -S php \  
php-pgsql \  
php-gd \  
php-fpm \  
php-composer \  
php-apcu-bc \  
wget \  
postgresql \  
git nodejs npm gcc-libs \  
pam shadow --noconfirm  
  
USER root  
RUN npm install uglify-js -g  
  
EXPOSE 9000  
  
VOLUME /srv/http  
  
RUN useradd -d /srv/http/ -s /bin/bash php && chown -R php:php /srv/http/  
RUN echo "php ALL = NOPASSWD: /opt/docker_owner.sh" >> /etc/sudoers  
  
COPY startup.sh /opt/  
COPY docker_owner.sh /opt/  
RUN chown php:php /opt/docker_owner.sh && chmod +x /opt/docker_owner.sh  
  
USER php  
ENTRYPOINT bash /opt/startup.sh  

