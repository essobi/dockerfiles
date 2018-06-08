FROM zabbix/zabbix-3.0:3.0.0  
  
ENV TZ=Asia/Tokyo  
  
RUN yum install -y ipa-pgothic-fonts \  
&& ln -s /usr/share/fonts/ipa-pgothic/ipagp.ttf
/usr/local/src/zabbix/frontends/php/fonts/ipagp.ttf \  
&& sed -i -e "/^define('ZBX_GRAPH_FONT_NAME',/c\define('ZBX_GRAPH_FONT_NAME',
'ipagp');" /usr/local/src/zabbix/frontends/php/include/defines.inc.php  

