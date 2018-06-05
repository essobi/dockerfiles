FROM resin/armv7hf-debian-qemu  
  
ENV RUN_AS_ROOT="true" \  
CHANGE_DIR_RIGHTS="false" \  
CHANGE_CONFIG_DIR_OWNERSHIP="true" \  
HOME="/config" \  
PLEX_DISABLE_SECURITY=1 \  
DEPS="xmlstarlet"  
VOLUME ["/config", "/data"]  
  
ADD ["Preferences.xml", "entrypoint", "dev2day-pms.gpg.key", "/"]  
  
EXPOSE 32400 1900 1900/udp 3005 5353 5353/udp 8324 32410 32410/udp 32412
32412/udp 32413 32413/udp 32414 32414/udp 32469  
RUN ["cross-build-start"]  
  
RUN echo "deb http://dev2day.de/pms/ jessie main" >
/etc/apt/sources.list.d/pms.list && \  
cat /dev2day-pms.gpg.key | apt-key add - && \  
apt-get update && \  
apt-get install -t jessie plexmediaserver ${DEPS} -y --force-yes && \  
apt-get autoremove && apt-get clean && apt-get autoclean && \  
rm -rf /var/cache/apk/* && \  
chmod +x /entrypoint  
  
RUN ["cross-build-end"]  
  
ENTRYPOINT ["/entrypoint"]

