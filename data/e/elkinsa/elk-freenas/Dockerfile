FROM sebp/elk  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.0.0.520" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.capabilities-add="NET_BROADCAST" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=5601 \  
org.freenas.web-ui-path="" \  
org.freenas.port-
mappings="5601:5601/tcp,5000:5000/tcp,5001:5001/tcp,514:514/tcp,9200:9200/tcp,514:514/udp"
\  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/transcode\", \  
\"descr\": \"Video transcode directory\" \  
}, \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Media volume\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Plex container Timezone\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ADVERTISE_IP\", \  
\"descr\": \"http://<hostIPAddress>:32400/\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ALLOWED_NETWORKS\", \  
\"descr\": \"IP/mask[,IP/mask]\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PLEX_UID\", \  
\"descr\": \"Plex User ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PLEX_GID\", \  
\"descr\": \"Plex Group ID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PLEX_CLAIM\", \  
\"descr\": \"Plex Account Token\", \  
\"optional\": true \  
} \  
]"  

