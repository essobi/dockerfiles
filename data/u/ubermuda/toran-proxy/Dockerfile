FROM debian:jessie  
MAINTAINER Geoffrey Bachelet <geoffrey.bachelet@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get install -y curl nginx php5-fpm php5-json daemontools  
  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf  
RUN sed -e 's/;listen\\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf  
RUN sed -e 's/;listen\\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
RUN mkdir -p /var/www  
RUN curl -sL https://toranproxy.com/releases/toran-proxy-v1.1.1.tgz | tar xzC
/var/www  
  
ADD vhost.conf /etc/nginx/sites-enabled/default  
ADD service/ /etc/service  
  
RUN chmod -R 777 /var/www/toran/app/cache /var/www/toran/app/logs  
  
EXPOSE 80  
#ENTRYPOINT ["svscan", "/srv/service"]  

