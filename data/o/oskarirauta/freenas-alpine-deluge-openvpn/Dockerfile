FROM oskarirauta/alpine-deluge-openvpn:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="Latest (Auto Update)" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8112 \  
org.freenas.web-ui-path="" \  
org.freenas.port-
mappings="8112:8112/tcp,58846:58846/tcp,58946:58946/tcp,58946:58946/udp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"Downloads volume\" \  
}, \  
{ \  
\"name\": \"/etc/openvpn/\", \  
\"descr\": \"ovpn config file storage\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone - eg Europe/London\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LOCAL_NETWORK\", \  
\"descr\": \"IP/mask[,IP/mask]\", \  
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

