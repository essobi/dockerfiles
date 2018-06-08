FROM alpine:3.6  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_LOGGING=1 \  
SERVICE_CRON="" \  
RESTORE_NAME="" \  
LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
TIME_ZONE=Europe/Moscow \  
TERM=xterm \  
VERSION=1  
RUN S6_OVERLAY_VERSION=v1.19.1.1 && \  
echo $TIME_ZONE > /etc/timezone && \  
apk add --no-cache bash nano ca-certificates curl rsnapshot && \  
rm -f /etc/rsnapshot.conf.default && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xz -C /  
  
ENTRYPOINT [ "/init" ]  
# VOLUME ["/backup"]  
VOLUME ["/var/log", "/data"]  
COPY root /  

