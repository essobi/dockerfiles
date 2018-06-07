FROM dreamcat4/jackett:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="9117" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="9117:9117/tcp,9118:9118/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Where jackett should store config files\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"jackett_uid\", \  
\"descr\": \"USER ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"jackett_gid\", \  
\"descr\": \"GROUP ID\", \  
\"optional\": true \  
} \  
]" \  

