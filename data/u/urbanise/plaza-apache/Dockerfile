FROM alpine  
  
RUN apk add --update apache2 apache2-proxy nmap-ncat && \  
rm /etc/apache2/conf.d/default.conf && \  
rm /etc/apache2/conf.d/userdir.conf && \  
rm /etc/apache2/conf.d/info.conf && \  
rm -rf /var/www/localhost/htdocs/index.html && \  
rm -rf /var/www/localhost/cgi-bin && \  
rm -rf /var/cache/apk/* && \  
mkdir /run/apache2 && \  
sed -i 's/^#LoadModule slotmem_shm_module .*$/LoadModule slotmem_shm_module
modules\/mod_slotmem_shm.so/g' /etc/apache2/httpd.conf &&\  
sed -i 's/^#LoadModule deflate_module .*$/LoadModule deflate_module
modules\/mod_deflate.so/g' /etc/apache2/httpd.conf &&\  
sed -i 's/^LoadModule proxy_fdpass_module .*$/#LoadModule proxy_fdpass_module
modules\/mod_proxy_fdpass.so/g' /etc/apache2/conf.d/proxy.conf  
  
COPY google0c671af6cca412de.html
/var/www/localhost/htdocs/google0c671af6cca412de.html  
COPY robots.txt /var/www/localhost/htdocs/robots.txt  
COPY leap.conf /etc/apache2/conf.d/leap.conf  
  
EXPOSE 80  
  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

