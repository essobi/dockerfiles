FROM resin/armv7hf-debian-qemu  
  
VOLUME ["/data", "/config"]  
  
EXPOSE 9091 51413 51413/udp  
  
COPY ["settings.json", "/config/"]  
  
RUN ["cross-build-start"]  
  
RUN apt-get update && apt-get install -y transmission-daemon && \  
rm -rf /var/cache/apk/*  
  
RUN ["cross-build-end"]  
  
ENTRYPOINT ["transmission-daemon", "--foreground", "--log-info", "--config-
dir", "/config"]

