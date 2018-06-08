FROM linuxserver/nextcloud:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="8080" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="8080:8080/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Where nextcloud should store config files\" \  
}, \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Where nextcloud should store data\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"USER ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GROUP ID\", \  
\"optional\": true \  
} \  
]"  

