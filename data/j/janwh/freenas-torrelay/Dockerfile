FROM vpetersson/torrelay:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="9001:9001/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/home/tor/.tor\", \  
\"descr\": \"Tor config directory\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"NICKNAME\", \  
\"descr\": \"Torrelay Nickname\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"CONTACTINFO\", \  
\"descr\": \"Admin contact info\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"ACCOUNTINGMAX\", \  
\"descr\": \"Maximum data transfer per month\", \  
\"optional\": true \  
} \  
]"  

