FROM alpine  
  
ENV INSTALL_PACKAGE ca-certificates tzdata php7 php7-zlib php7-curl
php7-openssl php7-zip php7-iconv  
  
RUN apk add --no-cache --update ${INSTALL_PACKAGE}  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone  
RUN sed -i "s/^doc_root\ =.*/doc_root = \/opt\/web/g" /etc/php7/php.ini \  
&& sed -i "s/^display_errors\ =.*/display_errors = On/g" /etc/php7/php.ini \  
&& sed -i "s/^;date\\.timezone\ =.*/date.timezone = Asia\/Shanghai/g"
/etc/php7/php.ini \  
&& mkdir -p /opt/web \  
&& echo "<?php phpinfo(); ?>" > /opt/web/index.php  
  
WORKDIR /opt  
CMD ["php7", "-S", "0.0.0.0:9000", "-t", "/opt/web"]

