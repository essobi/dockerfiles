FROM oskarirauta/alpine-transmission-openvpn:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="Latest (Auto Update)" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.privileged="false" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="9091" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="9091:9091/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/data/downloads\", \  
\"descr\": \"download location\" \  
}, \  
{ \  
\"name\": \"/data/incomplete\", \  
\"descr\": \"incomplete downloads location\" \  
}, \  
{ \  
\"name\": \"/data/watch\", \  
\"descr\": \"transmission watchdir location\" \  
}, \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"config storage space\" \  
}, \  
{ \  
\"name\": \"/etc/scripts\", \  
\"descr\": \"script folder\" \  
}, \  
{ \  
\"name\": \"/etc/openvpn/custom\", \  
\"descr\": \"ovpn config file storage\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LOCAL_NETWORK\", \  
\"descr\": \"IP/mask[,IP/mask] for e.g. 10.0.0.0/24\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_USERNAME\", \  
\"descr\": \"USERNAME\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_PASSWORD\", \  
\"descr\": \"PASSWORD\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_PROVIDER\", \  
\"descr\": \"PROVIDER\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_CONFIG\", \  
\"descr\": \"CONFIG\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"UserID\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"GroupID\", \  
\"optional\": true \  
} \  
]"  

