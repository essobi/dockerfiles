FROM pataquets/nginx-tls-proxy  
  
ADD files/etc/nginx/conf.d/ /etc/nginx/conf.d/  
  
RUN \  
mv -v \  
/etc/nginx/confs-available/tls-port-listen-http2 \  
/etc/nginx/conf.d/includes/tls-port-listen \  
&& \  
mv -v \  
/etc/nginx/confs-available/strip-www.conf \  
/etc/nginx/conf.d/  

