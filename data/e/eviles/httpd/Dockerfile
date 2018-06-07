FROM eviles/centos-sshd  
  
RUN yum -y install httpd \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& sed -i '/^#ServerName/cServerName localhost' /etc/httpd/conf/httpd.conf \  
&& sed -i 's/DirectoryIndex index.html/DirectoryIndex index.html index.htm/g'
/etc/httpd/conf/httpd.conf \  
&& echo "[program:httpd]" >> /etc/supervisord.conf \  
&& echo "command=/usr/sbin/httpd -D FOREGROUND" >> /etc/supervisord.conf  
  
EXPOSE 80 443  
VOLUME /var/www/html  

