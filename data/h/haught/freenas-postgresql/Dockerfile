FROM postgres:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.bridged="true" \  
org.freenas.port-mappings="5432:5432/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/var/lib/postgresql/data\", \  
\"descr\": \"PostgreSQL data space\" \  
}, \  
{ \  
\"name\": \"/etc/postgresql\", \  
\"descr\": \"Config space\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"LANG\", \  
\"descr\": \"Language eg, en_US.utf8\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGDATA\", \  
\"descr\": \"PostgreSQL data directory, eg /var/lib/postgresql/data\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PATH\", \  
\"descr\": \"Path string\", \  
\"optional\": true \  
} \  
]"  

