FROM ubuntu:13.10  
MAINTAINER Thomas B Homburg <thomas@homburg.dk>  
  
RUN apt-get update  
  
RUN apt-get -qy install nginx-full  
  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# Tell nginx not to daemonize  
RUN sed -i "1i daemon off;" /etc/nginx/nginx.conf  
  
RUN mkdir -p /var/cache/npm/data  
RUN mkdir -p /var/cache/npm/tmp  
  
ADD files/etc/nginx/conf.d/npm.conf /etc/nginx/conf.d/npm.conf  
ADD files/etc/nginx/sites-available/npm_cache /etc/nginx/sites-
available/npm_cache  
ADD files/etc/nginx/sites-enabled/npm_cache /etc/nginx/sites-enabled/npm_cache  
  
EXPOSE 80  
CMD "/usr/sbin/nginx"  

