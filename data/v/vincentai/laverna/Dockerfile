FROM debian:latest  
  
MAINTAINER vincent@autistici.org  
  
RUN apt-get update  
RUN apt-get install -y \  
git \  
supervisor \  
nginx  
  
RUN chown -R www-data:www-data /var/lib/nginx  
RUN rm /var/www/html/index.nginx-debian.html  
RUN git clone -b gh-pages https://github.com/Laverna/static-laverna
/var/www/html  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD laverna.conf /etc/supervisor/conf.d/laverna.conf  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 80  

