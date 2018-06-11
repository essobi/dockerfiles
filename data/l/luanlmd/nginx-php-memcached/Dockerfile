FROM ubuntu:18.04  
MAINTAINER Luan Almeida <luanlmd@gmail.com>  
  
RUN apt update  
RUN apt upgrade -y  
  
RUN apt install ca-certificates curl nano -y  
RUN apt install memcached -y  
RUN apt install nginx -y  
RUN apt install php php-fpm php-dom php-mbstring php-memcached -y  
  
RUN useradd docker  
RUN adduser www-data docker  
  
CMD /etc/init.d/memcached start && /etc/init.d/php7.1-fpm start && nginx -g
"daemon off;"  

