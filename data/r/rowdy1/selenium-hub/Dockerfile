FROM selenium/hub:3.4.0-einsteinium  
LABEL org.freenas.interactive="false" \  
org.freenas.command="/opt/bin/entry_point.sh" \  
org.freenas.version="3.4.0-einsteinium" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="4444:4444/tcp" \  
org.freenas.privileged="false" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"GRID_MAX_SESSION\", \  
\"descr\": \"As integer, maps to 'maxSession' DEFAULT=5\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_NEW_SESSION_WAIT_TIMEOUT\", \  
\"descr\": \"In milliseconds, maps to 'newSessionWaitTimeout' DEFAULT=-1\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_THROW_ON_CAPABILITY_NOT_PRESENT\", \  
\"descr\": \"As a boolean, maps to 'throwOnCapabilityNotPresent'
DEFAULT=true\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_JETTY_MAX_THREADS\", \  
\"descr\": \"As an integer DEFAULT=-1\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_CLEAN_UP_CYCLE\", \  
\"descr\": \"In milliseconds, maps to 'cleanUpCycle' DEFAULT=5000\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_BROWSER_TIMEOUT\", \  
\"descr\": \"In seconds, maps to 'browserTimeout' DEFAULT=0\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_TIMEOUT\", \  
\"descr\": \"In seconds, maps to 'timeout' DEFAULT=30\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"GRID_DEBUG\", \  
\"descr\": \"Debug DEFAULT=false\", \  
\"optional\": true \  
} \  
]"

