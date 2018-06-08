FROM freeipa/freeipa-server:centos-7  
LABEL org.freenas.interactive="false" \  
org.freenas.privileged="true" \  
org.freenas.version="0.1.0" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="https" \  
org.freenas.web-ui-port="" \  
org.freenas.web-ui-path="" \  
org.freenas.port-
mappings="53:53/udp,53:53/tcp,80:80/tcp,443:443/tcp,389:389/tcp,636:636/tcp,88:88/tcp,88:88/udp,464:464/tcp,464:464/udp,123:123/udp,7389:7389/tcp,9443:9443/tcp,9444:9444/tcp,9445:9445/tcp"
\  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/data\", \  
\"descr\": \"FreeIPA data\" \  
}, \  
{ \  
\"name\": \"/var/log/journal\", \  
\"descr\": \"FreeIPA logs\" \  
}, \  
{ \  
\"name\": \"/run\", \  
\"descr\": \"FreeIPA run\" \  
}, \  
{ \  
\"name\": \"/tmp\", \  
\"descr\": \"FreeIPA tmp\" \  
} \  
]"  

