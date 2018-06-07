FROM haproxy:1.6  
MAINTAINER Ed Marshall <ed.marshall@infinityworks.com>  
  
ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
CMD sed -ri 's/CADVISOR_HOST_IP/'"$CADVISOR_HOST_IP"'/g'
/usr/local/etc/haproxy/haproxy.cfg;exec haproxy -db -f
/usr/local/etc/haproxy/haproxy.cfg  
  
EXPOSE 9104  

