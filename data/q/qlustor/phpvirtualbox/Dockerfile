#BUILDS qlustor/phpvirtualbox  
FROM qlustor/nginx-php-fpm  
MAINTAINER Team QLUSTOR <team@qlustor.com>  
  
# Install phpvirtualbox  
ENV PHPVBOX_BUILD phpvirtualbox-5.0-5  
ENV PHPVBOX_DLURL
http://sourceforge.net/projects/phpvirtualbox/files/$PHPVBOX_BUILD.zip/download  
RUN apk-install --update ca-certificates \  
&& update-ca-certificates \  
&& apk-install wget unzip \  
&& wget $PHPVBOX_DLURL -O /var/$PHPVBOX_BUILD.zip \  
&& unzip /var/$PHPVBOX_BUILD.zip -d /var \  
&& mv /var/$PHPVBOX_BUILD/* /var/www \  
&& chown -R nginx:nginx /var/www/* \  
&& rm -f /var/$PHPVBOX_BUILD.zip \  
&& rm -rf /var/$PHPVBOX_BUILD  
  
ADD . /  
  
EXPOSE 80  
ENTRYPOINT php /servers-from-env.php && /sbin/runit-docker  
  

