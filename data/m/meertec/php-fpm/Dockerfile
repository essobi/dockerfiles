FROM meertec/archlinux:latest  
  
MAINTAINER meertec <mail@meertec.de>  
  
# persistent / runtime deps  
# no image magick because its use a lot of packages to compile  
RUN pacman -Syy; pacman -S php-fpm php-ldap php-intl php-gd php-pgsql
--noconfirm;rm -rf /var/cache/pacman/pkg;  
ADD php /etc/php  
VOLUME ["/etc/php"]  
  
EXPOSE 9000  
CMD ["/usr/bin/php-fpm","-F"]  

