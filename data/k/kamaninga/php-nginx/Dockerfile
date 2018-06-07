FROM kamaninga/php  
  
ENV WEB_DOCUMENT_ROOT=/application \  
WEB_DOCUMENT_INDEX=index.php \  
WEB_ALIAS_DOMAIN=*.vm  
ENV WEB_PHP_SOCKET=127.0.0.1:9000  
  
COPY conf/ /opt/docker/  
  
RUN /usr/local/bin/apk-install \  
nginx \  
&& /opt/docker/bin/provision run \--tag bootstrap --role webdevops-nginx
--role webdevops-php-nginx \  
&& /opt/docker/bin/bootstrap.sh \  
&& docker-image-cleanup  
  
EXPOSE 80 443  

