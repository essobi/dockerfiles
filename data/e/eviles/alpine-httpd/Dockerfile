FROM eviles/alpine-sshd  
  
RUN apk --update add apache2 apache2-utils apache2-proxy \  
&& rm -rf /var/cache/apk/* \  
&& sed -i '/^#ServerName/cServerName localhost' /etc/apache2/httpd.conf \  
&& sed -i 's/DirectoryIndex index.html/DirectoryIndex index.html index.htm /g'
/etc/apache2/httpd.conf \  
&& echo "[program:httpd]" >> /etc/supervisord.conf \  
&& echo "command=/usr/sbin/httpd -D FOREGROUND" >> /etc/supervisord.conf \  
# Fix some error...  
&& mkdir /run/apache2 \  
&& addgroup -S apache \  
&& sed -i 's/^#LoadModule slotmem_shm_module/LoadModule slotmem_shm_module/g'
/etc/apache2/httpd.conf  
  
EXPOSE 80 443  
VOLUME /var/www/localhost/htdocs  

