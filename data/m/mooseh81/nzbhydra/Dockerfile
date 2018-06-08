FROM linuxserver/hydra:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="5075" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="5075:5075/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Where hydra should store config files\" \  
}, \  
{ \  
\"name\": \"/downloads\", \  
\"descr\": \"NZB download folder\" \  
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

