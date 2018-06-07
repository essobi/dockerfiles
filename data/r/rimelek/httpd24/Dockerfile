FROM httpd:2.4  
  
LABEL maintainer="rimelek@it-sziget.hu"  
  
ENV SRV_REVERSE_PROXY_DOMAIN="" \  
SRV_REVERSE_PROXY_CLIENT_IP_HEADER=X-Forwarded-For \  
SRV_SSL=0 \  
SRV_AUTH=0 \  
SRV_ADMIN="" \  
SRV_NAME="" \  
SRV_DOCROOT="" \  
SRV_PHP=0 \  
SRV_PHP_HOST=php \  
SRV_PHP_PORT=9000  
  
COPY apache2 /usr/local/apache2  
  
RUN chmod +x /usr/local/apache2/bin/start.sh  
  
EXPOSE 80 443  
  
CMD ["/usr/local/apache2/bin/start.sh"]

