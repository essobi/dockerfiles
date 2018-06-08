FROM alpine  
  
RUN apk add --update --no-cache \  
curl \  
lighttpd \  
php5-common \  
php5-cgi \  
fcgi \  
openrc \  
&& rm -rf /var/cache/apk/*  
  
RUN echo "include \"mod_fastcgi.conf\"" >> /etc/lighttpd/lighttpd.conf  
  
RUN mkdir -p /run/lighttpd \  
&& chown lighttpd /run/lighttpd  
  
COPY index.php /var/www/localhost/htdocs/index.php  
RUN chown lighttpd /var/www/localhost/htdocs/index.php  
  
COPY start.sh /start.sh  
CMD /start.sh  

