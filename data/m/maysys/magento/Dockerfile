#  
# Create the container for Magento with Magento memory requirements  
#  
FROM m2i3/nginx-php5:latest  
MAINTAINER Jean-Marc Lagacé <jmlagace@maysys.com>  
  
ENV MAGE_RUN_CODE="default" MAGE_RUN_TYPE="store"  
RUN rm /usr/share/nginx/html/*  
  
RUN pear install Net_GeoIP  
  
ENV NGINX_WORKER_PROCESS=1 \  
NGINX_WORKER_CONNECTIONS=2048 \  
PHP_MEMORY_LIMIT=512M \  
MAX_UPLOAD_SIZE=1M \  
PHP_MAX_CHILDREN=100 \  
PHP_MAX_REQUESTS=500 \  
PHP_EMERGENCY_RESTART_THRESHOLD=20 \  
MAGENTO_VERSION=1.9.0.1  
EXPOSE 80  
COPY nginx-site.conf /etc/nginx/sites-available/default  
COPY 500-setenvironment.sh /usr/lib/startup.d/  
COPY SUPEE/* /tmp/SUPEE/  
RUN chmod +x /usr/lib/startup.d/* \  
&& chmod +x /tmp/SUPEE/*  
  
VOLUME /usr/share/nginx/html/media/ \  
/usr/share/nginx/html/var/log/ \  
/usr/share/nginx/html/var/report/ \  
/usr/share/nginx/html/var/session/ \  
/etc/magento  
  
RUN cd /tmp \  
&& curl -o magento.tar.gz https://codeload.github.com/OpenMage/magento-
mirror/tar.gz/$MAGENTO_VERSION \  
&& tar -xzf magento.tar.gz \  
&& cp -r /tmp/magento-mirror-$MAGENTO_VERSION/. /usr/share/nginx/html/ \  
&& cp /tmp/SUPEE/PATCH_* /usr/share/nginx/html/ \  
&& bash -c 'cd /usr/share/nginx/html/; for i in `ls PATCH_*`; do echo applying
$i && ./$i; done' \  
&& rm /usr/share/nginx/html/PATCH_SUPEE-* \  
&& chown -R www-data:www-data /usr/share/nginx/html/. \  
&& rm -rf /tmp/*  
  
# uneeded until you go to production (i.e. with a client specific image)  
#RUN php /usr/share/nginx/html/shell/compiler.php compile  
# these should be added in the script specific to the client  
#ONBUILD COPY ./src /usr/share/nginx/html/  
#ONBUILD RUN php /usr/share/nginx/html/shell/compiler.php compile  

