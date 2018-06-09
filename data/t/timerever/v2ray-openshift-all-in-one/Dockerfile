from nginx:latest  
  
ENV CLIENT_ID 00000000-0000-0000-0000-000000000000  
ENV CLIENT_ALTERID 64  
ENV CLIENT_SECURITY aes-128-gcm  
  
ADD conf/nginx.conf /etc/nginx/  
ADD conf/default.conf /etc/nginx/conf.d/  
ADD v2ray /usr/local/bin/  
ADD entrypoint.sh /etc/  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends php-fpm php-curl php-cli php-
mcrypt php-mysql php-readline \  
&& chmod -R 777 /var/log/nginx /var/cache/nginx /var/run \  
&& chgrp -R 0 /etc/nginx \  
&& chmod -R g+rwx /etc/nginx \  
&& mkdir /run/php/ \  
&& chmod -R 777 /var/log/ /run/php/ \  
&& mkdir /var/log/v2ray \  
&& mkdir /etc/v2ray \  
&& chmod 777 /usr/local/bin/v2ray \  
&& chmod -R 777 /var/log/v2ray \  
&& chmod -R 777 /etc/v2ray \  
&& chmod 777 /etc/entrypoint.sh \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/apt/*  
  
ADD conf/config.json /etc/v2ray/  
ADD conf/www.conf /etc/php/7.0/fpm/pool.d/  
ADD src/tz.php /usr/share/nginx/html/  
  
EXPOSE 8080  
ENTRYPOINT ["/etc/entrypoint.sh"]  

