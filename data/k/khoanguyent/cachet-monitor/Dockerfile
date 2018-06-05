FROM alpine:3.5  
ARG CACHET_MONITOR_VER=v3.0  
LABEL description="Monitoring Plugin for CachetHQ" \  
maintainer="Khoa Nguyen <khoa.tan.nguyen.96@gmail.com"  
  
RUN NB_CORES=${BUILD_CORES-`getconf _NPROCESSORS_CONF`} \  
&& BUILD_DEPS=" \  
wget" \  
&& apk -U upgrade && apk add \  
${BUILD_DEPS} \  
ca-certificates  
  
RUN adduser -S cachet  
  
RUN cd /tmp \  
&& wget https://github.com/CastawayLabs/cachet-
monitor/releases/download/${CACHET_MONITOR_VER}/cachet_monitor_linux_amd64 \  
&& cp cachet_monitor_linux_amd64 /usr/bin/cachet-monitor \  
&& chmod +x /usr/bin/cachet-monitor \  
&& mkdir /config \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
USER cachet  
  
VOLUME /config  
  
ENTRYPOINT ["/usr/bin/cachet-monitor", "-c", "/config/cachet-
monitor.config.json"]

