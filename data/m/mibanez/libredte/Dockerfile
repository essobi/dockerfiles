FROM mibanez/libredte-base:latest  
  
RUN wget -c https://github.com/SowerPHP/sowerpkg/raw/master/sowerpkg.sh -P
/tmp \  
&& chmod +x /tmp/sowerpkg.sh \  
&& /tmp/sowerpkg.sh install -e "app general" -W \  
&& rm /tmp/sowerpkg.sh \  
&& git clone \--recursive https://github.com/LibreDTE/libredte-webapp.git
/var/www/html/libredte \  
&& cd /var/www/html/libredte/website \  
&& $HOME/bin/composer install \  
&& mkdir -p /data/logos \  
&& mkdir -p /data/firma_electronica \  
&& chmod -R a+rw /data  
# Setting config file with default values  
  
COPY core.php /var/www/html/libredte/website/Config/core.php  

