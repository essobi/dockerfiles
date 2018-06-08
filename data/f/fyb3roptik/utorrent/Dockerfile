FROM fyb3roptik/utorrent-freenas:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="5" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="2222" \  
org.freenas.web-ui-path="gui" \  
org.freenas.port-mappings="2222:2222/tcp,6881:6881/tcp,6881:6881/udp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/utorrent\", \  
\"descr\": \"Watch folder for torrent files\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone - eg America/Chicago\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
} \  
]"  

