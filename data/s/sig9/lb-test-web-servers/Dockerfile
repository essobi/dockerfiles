FROM alpine:3.5  
RUN apk --no-cache add apache2 php7-apache2 \  
&& mkdir -p /run/apache2/ \  
&& rm -f /var/www/localhost/htdocs/index.html \  
&& sed -i 's/ DirectoryIndex index.html/ DirectoryIndex index.php/g'
/etc/apache2/httpd.conf  
COPY files/favicon.ico /var/www/localhost/htdocs/favicon.ico  
COPY files/index.php /var/www/localhost/htdocs/index.php  
COPY files/hostname.php /var/www/localhost/htdocs/hostname.php  
COPY files/time.php /var/www/localhost/htdocs/time.php  
ENV LB_NODE=Web  
ENV LB_COLOR=red  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

