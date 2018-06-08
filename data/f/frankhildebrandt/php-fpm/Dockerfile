FROM php:7.0-fpm  
MAINTAINER Frank Hildebrandt <frank@openworkers.de>  
  
RUN apt-get update \  
&& apt-get install -y nginx \  
&& curl
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego -o /usr/local/bin/forego \  
&& chmod u+x /usr/local/bin/forego \  
&& echo "\ndaemon off;" >> /etc/nginx/nginx.conf \  
&& echo "\nerror_log /dev/stdout warn;" >> /etc/nginx/nginx.conf \  
&& apt-get clean  
  
WORKDIR /  
  
ADD . /root  
  
RUN mv /root/upstream.conf /etc/nginx/conf.d/upstream.conf \  
&& mv /root/nginx_vhost.conf /etc/nginx/sites-enabled/default \  
&& mv /root/index.php /var/www/html/index.php \  
&& mv /root/Procfile /  
  
EXPOSE 80  
CMD ["forego", "start"]

