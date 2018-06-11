FROM nginx:1.9.9  
MAINTAINER Fabian Stegemann <fabian.stegemann@gmx.net>  
  
ADD nginx-vhost.conf /etc/nginx/conf.d/default.conf  
ADD start-nginx.sh /usr/bin/start-nginx  
  
CMD ["/usr/bin/start-nginx"]  

