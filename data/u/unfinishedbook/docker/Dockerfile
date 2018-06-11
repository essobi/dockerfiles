FROM zabbix/zabbix-web-nginx-mysql:alpine-3.2-latest  
  
COPY localtime /etc/localtime  
COPY simkai.ttf /usr/share/zabbix/fonts  
  
RUN sed -i "/ZBX_GRAPH_FONT_NAME/ s/graphfont/simkai/"
/usr/share/zabbix/include/defines.inc.php  
RUN sed -i "/listen/ s/80/8888/" /etc/zabbix/nginx.conf  
  

