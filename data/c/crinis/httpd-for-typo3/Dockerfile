FROM httpd:2.4-alpine  
  
ENV TZ="Europe/Berlin" \  
SERVER_ADMIN_EMAIL="you@example.com" \  
PHP_FPM="php:9000" \  
CODE_DIR="/code" \  
PUBLIC_DIR="/code/public"  
  
COPY httpd-custom.conf /usr/local/apache2/conf/extra  
COPY docker-httpd-for-typo3-entrypoint.sh /usr/local/bin/docker-httpd-for-
typo3-entrypoint.sh  
  
RUN set -xe \  
&& apk add --no-cache nano tzdata \  
&& sed -i '/LoadModule proxy_module/s/#//g' /usr/local/apache2/conf/httpd.conf
\  
&& sed -i '/LoadModule proxy_fcgi_module/s/#//g'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i '/LoadModule rewrite_module/s/#//g'
/usr/local/apache2/conf/httpd.conf \  
&& sed -i '/User daemon/c\User www-data' /usr/local/apache2/conf/httpd.conf \  
&& sed -i '/Group daemon/c\Group www-data' /usr/local/apache2/conf/httpd.conf
\  
&& sed -i -e "\$aInclude conf\/extra\/httpd-custom.conf"
/usr/local/apache2/conf/httpd.conf \  
&& chmod +x /usr/local/bin/docker-httpd-for-typo3-entrypoint.sh  
  
WORKDIR $CODE_DIR  
  
ENTRYPOINT ["docker-httpd-for-typo3-entrypoint.sh"]  
  
CMD ["httpd-foreground"]  

