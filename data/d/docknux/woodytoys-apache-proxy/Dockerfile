FROM httpd:2.4-alpine  
MAINTAINER Denis Pettens <denis.pettens@gmail.com>  
  
# Install apache2-ssl  
RUN set -x \  
&& apk update \  
&& apk add --upgrade apache2-ssl \  
&& rm -rf /var/cache/apk/*  
  
# ServerRoot of apache  
WORKDIR /usr/local/apache2  
  
# Enable ssl, rewrite, proxy and proxy_http modules  
RUN set -x \  
&& sed -i 's/^#LoadModule ssl_module modules\/mod_ssl.so/LoadModule ssl_module
modules\/mod_ssl.so/' conf/httpd.conf \  
&& sed -i 's/^#LoadModule rewrite_module modules\/mod_rewrite.so/LoadModule
rewrite_module modules\/mod_rewrite.so/' conf/httpd.conf \  
&& sed -i 's/^#LoadModule proxy_module/LoadModule proxy_module/'
conf/httpd.conf \  
&& sed -i 's/^#LoadModule proxy_http_module/LoadModule proxy_http_module/'
conf/httpd.conf  
  
# Enable Listen on port 443  
RUN set -x \  
&& sed -i '/Listen 80/aListen 443\n' conf/httpd.conf  
  
# Set default ServerAdmin and load virtualhost configurations  
RUN set -x \  
&& sed -i 's/^ServerAdmin you@example.com/ServerAdmin sysadmin@wt6.ephec-
ti.com/' conf/httpd.conf \  
&& sed -i 's/^#Include conf\/extra\/httpd-vhosts.conf/IncludeOptional
conf\/vhosts\/*.conf/' conf/httpd.conf \  
&& mkdir conf/vhosts  
  
COPY vhosts/*.conf conf/vhosts/  
  
EXPOSE 80  
EXPOSE 443  
CMD ["httpd-foreground"]  

