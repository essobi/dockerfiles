FROM francescou/docker-compose-ui:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="1" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="5000:5000/tcp" \  
org.freenas.privileged="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=5000 \  
org.freenas.web-ui-path="" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/opt/docker-compose-projects\", \  
\"descr\": \"Compose Projects directory\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"GIT_REPO\", \  
\"descr\": \"Optional Git Repository\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"DOCKER_HOST\", \  
\"descr\": \"Remote docker host and port\", \  
\"optional\": true \  
} \  
]"  
  

