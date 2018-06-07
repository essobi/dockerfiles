FROM khipu/base-alpine-s6:edge  
MAINTAINER developers@khipu.com  
  
RUN apk add --update zabbix-pgsql=3.0.3-r0 zabbix-webif=3.0.3-r0 zabbix-
utils=3.0.3-r0 nginx php5-fpm php5-ldap php5-pgsql jq bash fping tzdata \  
&& cp /usr/share/zoneinfo/America/Santiago /etc/localtime \  
&& echo "America/Santiago" > /etc/timezone \  
&& apk del tzdata \  
&& rm -rf /var/cache/apk/* \  
&& chmod -R 755 /var/lib/nginx \  
&& mkdir /run/nginx/ \  
&& sed -i 's/date.timezone = UTC/date.timezone = America\/Santiago/g'
/etc/php5/php.ini  
  
ADD zabbix-server.sh /etc/services.d/zabbix-server/run  
ADD nginx.sh /etc/services.d/nginx/run  
ADD php-fpm.sh /etc/services.d/php-fpm/run  
  
ADD confd /etc/confd  
  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/php-fpm.conf /etc/php5/php-fpm.conf  
  
RUN echo "always_populate_raw_post_data = -1" >> /etc/php5/php.ini  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

