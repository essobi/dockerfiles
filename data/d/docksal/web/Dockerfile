FROM httpd:2.4-alpine  
  
# Generate a self-signed cert  
RUN apk add --no-cache openssl \  
&& openssl req -batch -x509 -newkey rsa:4096 -days 3650 -nodes -sha256 \  
-keyout /usr/local/apache2/conf/server.key -out /usr/local/apache2/conf/server.crt \  
&& apk del openssl  
  
# Configure Apache environment variables  
ENV \  
APACHE_DOCUMENTROOT=/var/www/docroot \  
APACHE_FCGI_HOST_PORT="cli:9000"  
  
RUN set -x \  
# Enabled extra modules  
&& sed -i '/^#.* proxy_module /s/^#//' /usr/local/apache2/conf/httpd.conf \  
&& sed -i '/^#.* proxy_http_module /s/^#//' /usr/local/apache2/conf/httpd.conf
\  
&& sed -i '/^#.* proxy_fcgi_module /s/^#//' /usr/local/apache2/conf/httpd.conf
\  
&& sed -i '/^#.* proxy_connect_module /s/^#//'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i '/^#.* ssl_module /s/^#//' /usr/local/apache2/conf/httpd.conf \  
&& sed -i '/^#.* socache_shmcb_module /s/^#//'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i '/^#.* rewrite_module /s/^#//' /usr/local/apache2/conf/httpd.conf \  
# Enable extra config files  
&& sed -i '/^#.* conf\/extra\/httpd-vhosts.conf/s/^#//'
/usr/local/apache2/conf/httpd.conf \  
# Used for runtime config overrides  
&& mkdir -p /usr/local/apache2/conf/custom \  
# Link out custom docroot location to the default htdocs folder by default  
&& mkdir -p /var/www \  
&& ln -s /usr/local/apache2/htdocs $APACHE_DOCUMENTROOT  
  
COPY httpd-foreground /usr/local/bin/  
COPY conf /usr/local/apache2/conf  
  
WORKDIR /var/www  
  
EXPOSE 80 443  
  
CMD ["httpd-foreground"]  

