FROM meertec/archlinux:latest  
  
MAINTAINER Maintaner meertec <mail@meertec.de>  
  
RUN pacman -Syy; pacman -S nginx --noconfirm;rm -rf /var/cache/pacman/pkg;  
ADD configs/nginx.conf /etc/nginx/  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log;ln -sf /dev/stderr
/var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx", "/etc/nginx", "/usr/share/nginx/html"]  
EXPOSE 80 443  
CMD ["nginx"]  
  

