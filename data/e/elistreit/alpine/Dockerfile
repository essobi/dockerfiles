FROM elistreit/alpine  
  
LABEL name "es-docker-alpine"  
LABEL version "0.1.0"  
LABEL maintainer "Eli Streit — https://t.me/elistreit"  
  
RUN apk upgrade --no-cache --purge --available  
RUN rm -rf /tmp/* && rm -rf /var/cache/apk/*  
  
ONBUILD ENV ECHO "printf
\n\n\033[1;30m[Dockerfile]\t\033[1;32m%s\033[0m\n\n\n"  
ONBUILD RUN \  
$ECHO "ONBUILD: Updating Apline distro..." \  
; apk upgrade --no-cache --purge --available  
  
ONBUILD RUN \  
$ECHO "ONBUILD: Clean up after updating..." \  
; rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  

