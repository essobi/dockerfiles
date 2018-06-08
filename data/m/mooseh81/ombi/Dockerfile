FROM linuxserver/ombi:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="3579" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="3579:3579/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Where ombi should store config files\" \  
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
]" \  

