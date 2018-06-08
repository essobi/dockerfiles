FROM labengine/ubuntu  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# Env resilio Download  
ENV RESILIO_V stable  
ENV LINK https://download-cdn.resilio.com/${RESILIO_V}/linux-x64/resilio-
sync_x64.tar.gz  
  
# Download and decompress rlsync to directory  
ADD ${LINK} /tmp/sync.tgz  
RUN tar -xf /tmp/sync.tgz -C /usr/bin rslsync && rm -f /tmp/sync.tgz  
  
# Copy script to run resilio  
COPY scripts/rslsync.conf /etc/  
COPY scripts/rslsync.sh /opt/  
  
# fix permission to run "rslsync.sh"  
RUN chmod 777 /opt/*.sh  
  
# Work dir  
WORKDIR /sync  
  
# Directory sync  
VOLUME ["/sync", "/sync/config", "/sync/folders"]  
  
# Port expose 8888 is webui  
EXPOSE 8888  
EXPOSE 55555  
# Command start rlsync  
ENTRYPOINT ["/opt/rslsync.sh"]  
CMD ["--config", "/etc/rslsync.conf"]  

