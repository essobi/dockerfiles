FROM million12/haproxy:latest  
RUN yum install -y bind-utils, which, httpd  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="80:80/tcp,443:443/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/etc/haproxy/ \", \  
\"descr\": \"HA Proxy Config\" \  
} \  
]"  

