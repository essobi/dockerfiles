FROM chuckremes/docker-openvpn-client:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="false" \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Location to store custom ovpn files (optional).\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"OPENVPN_PROVIDER\", \  
\"descr\": \"Name of VPN provider, must match list exactly.\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_USERNAME\", \  
\"descr\": \"Configure username for VPN provider.\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_PASSWORD\", \  
\"descr\": \"Configure password for VPN provider.\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_CONFIG\", \  
\"descr\": \"Set VPN provider endpoint, e.g. UK Southampton.\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"OPENVPN_OPTS\", \  
\"descr\": \"Command line switches to be passed directly to openvpn upon
startup.\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"LOCAL_NETWORK\", \  
\"descr\": \"Sets local network that should have access to VPN, e.g.
192.168.18.0/24.\", \  
\"optional\": true \  
} \  
]"  

