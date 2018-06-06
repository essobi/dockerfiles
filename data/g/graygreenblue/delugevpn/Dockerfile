FROM binhex/arch-delugevpn:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1.3.14" \  
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
\"host_path\": \"/mnt/tank/appdata/delugevpn\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/seedbox\", \  
\"descr\": \"Downloads volume\" \  
} \  
]" \  
org.freenas.static-volumes="[ \  
{ \  
\"container_path\": \"/etc/localtime\", \  
\"host_path\": \"/etc/localtime\", \  
\"readonly\": \"true\" \  
} \  
]" \  
org.freenas.settings="[ \ \  
{ \  
\"env\": \"VPN_ENABLED\", \  
\"value\": \"yes\", \  
\"descr\": \"Enable VPN? <yes|no>\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_USER\", \  
\"descr\": \"VPN Username\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_PASS\", \  
\"descr\": \"VPN Password\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_REMOTE\", \  
\"descr\": \"VPN Remote Gateway\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_PORT\", \  
\"descr\": \"VPN Port\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_PROTOCOL\", \  
\"descr\": \"VPN Remote Protocol\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_DEVICE_TYPE\", \  
\"descr\": \"VPN Device Type <tun|tap>\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_PROV\", \  
\"descr\": \"VPN Provider <pia|airvpn|custom>\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"VPN_OPTIONS\", \  
\"descr\": \"Additional VPN Options\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"STRONG_CERTS\", \  
\"descr\": \"Strong Certs? <yes|no>\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"ENABLE_PRIVOXY\", \  
\"descr\": \"Enable Privoxy? <yes|no>\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"LAN_NETWORK\", \  
\"descr\": \"LAN Network to allow traffic through, <lan ipv4 network>/<cidr
notation> eg. 192.168.0.0/16\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"NAME_SERVERS\", \  
\"descr\": \"DNS Server ip(s) for VPN\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DEBUG\", \  
\"descr\": \"Debug mode? <true|false>\", \  
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

