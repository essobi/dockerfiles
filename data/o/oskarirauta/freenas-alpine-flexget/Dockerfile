FROM oskarirauta/alpine-flexget:latest  
LABEL org.freenas.interactive="false" \  
org.freenas.version="Latest (Auto Update)" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port=3539 \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="3539:3539/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Config storage space\" \  
}, \  
{ \  
\"name\": \"/data/downloads\", \  
\"descr\": \"Finished downloads location\" \  
}, \  
{ \  
\"name\": \"/data/incomplete\", \  
\"descr\": \"Incomplete downloads location\" \  
}, \  
{ \  
\"name\": \"/media/series\", \  
\"descr\": \"Location for series\" \  
}, \  
{ \  
\"name\": \"/media/movies\", \  
\"descr\": \"Location for movies\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"TZ\", \  
\"descr\": \"Timezone - eg Europe/Helsinki\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"PUID\", \  
\"descr\": \"User ID\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"PGID\", \  
\"descr\": \"Group ID\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"WEBUI_PASSWORD\", \  
\"descr\": \"FlexGet WebUI Password\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"TRAKT_USERID\", \  
\"descr\": \"Trakt account userid\", \  
\"optional\": true \  
} \  
]"  

