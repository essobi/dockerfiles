FROM alpine  
  
ARG S6_OVERLAY_VERSION=1.21.4.0  
ARG S6_OVERLAY_ARCH=x86  
ENV S6_LOGGING_SCRIPT=T  
  
# download and install s6  
RUN apk --no-cache add curl &&\  
curl -L https://github.com/just-
containers/s6-overlay/releases/download/v$S6_OVERLAY_VERSION/s6-overlay-$S6_OVERLAY_ARCH.tar.gz
-o /tmp/s6-overlay.tar.gz &&\  
tar xzf /tmp/s6-overlay.tar.gz -C / &&\  
rm /tmp/s6-overlay.tar.gz &&\  
apk --no-cache del curl  
  
# mandated by s6-overlay, do not override in children images  
ENTRYPOINT ["/init"]  

