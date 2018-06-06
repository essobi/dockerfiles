FROM openhab/openhab:2.1.0-amd64  
LABEL org.freenas.interactive="false" \  
org.freenas.version="2.1.0" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.capabilities-add="NET_BROADCAST" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=8080 \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="8080:8080/tcp,8443:8443/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/openhab/conf\", \  
\"descr\": \"Configuration directory\" \  
}, \  
{ \  
\"name\": \"/openhab/userdata\", \  
\"descr\": \"Userdata directory\" \  
}, \  
{ \  
\"name\": \"/openhab/addons\", \  
\"descr\": \"Addon directory\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Container Timezone\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"USER_ID\", \  
\"descr\": \"OpenHAB User ID\", \  
\"optional\": true \  
} \  
]"  

