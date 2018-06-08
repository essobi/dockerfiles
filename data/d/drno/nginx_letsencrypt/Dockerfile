FROM debian  
  
MAINTAINER Michael Feller <admin@profdrno.de>  
  
RUN echo "deb http://http.debian.net/debian jessie main" >>
/etc/apt/sources.list && echo "deb http://ftp.debian.org/debian jessie-
backports main" >> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y nginx nano dos2unix && apt-get install -y certbot -t
jessie-backports  
  
RUN mkdir -p /var/www/ssl/  
ADD default /etc/nginx/sites-available/  
  
ADD new_nginx.conf /etc/nginx  
  
EXPOSE 443 80  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
RUN dos2unix /start.sh && apt-get --purge remove -y dos2unix && apt-get clean
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /start.sh && service nginx start  

