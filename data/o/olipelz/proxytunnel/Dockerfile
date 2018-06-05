FROM alpine:latest  
MAINTAINER oliverpelz@gmail.com  
  
RUN apk add --no-cache nmap-ncat  
  
ENTRYPOINT ncat --sh-exec 'ncat --proxy $PROXY_SERVER:$PROXY_PORT
$TARGET_SERVER $TARGET_PORT' -l $LOCAL_PORT \--keep-open  

