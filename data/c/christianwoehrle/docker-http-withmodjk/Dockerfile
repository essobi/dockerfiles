FROM httpd:2.4  
RUN apt-get update && apt-get install -y telnet netstat vim less  
COPY setup/mod_jk.so /usr/local/apache2/modules/  
COPY setup/myhttpd.conf /usr/local/apache2/conf/httpd.conf  
RUN mkdir /usr/local/apache2/conf/mod_jk  
COPY setup/mod_jk.conf setup/workers.properties setup/vhostDude.conf
/usr/local/apache2/conf/mod_jk/  
COPY setup/restart.sh setup/main setup/start.sh /usr/local/apache2/bin/  
RUN mkdir /mod_jk_conf_update  
VOLUME /mod_jk_conf_update/  
CMD ["/usr/local/apache2/bin/start.sh"]  
  

