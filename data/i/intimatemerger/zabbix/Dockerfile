FROM zabbix/zabbix-3.0:3.0.0  
  
ENV TZ=Asia/Tokyo \  
PHP_date_timezone=Asia/Tokyo  
  
RUN yum install -y ipa-pgothic-fonts \  
&& ln -s /usr/share/fonts/ipa-pgothic/ipagp.ttf
/usr/local/src/zabbix/frontends/php/fonts/ipagp.ttf \  
&& sed -i -e 's/DejaVuSans/ipagp/g'
/usr/local/src/zabbix/frontends/php/include/defines.inc.php  

