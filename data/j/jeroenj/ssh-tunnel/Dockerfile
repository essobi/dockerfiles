FROM alpine:3.6  
  
RUN apk add \--update --no-cache autossh && \  
addgroup -S -g 987 tunnel && \  
adduser -S -u 987 -G tunnel tunnel  
  
USER tunnel  
  
VOLUME "/ssh_identity"  
  
ENTRYPOINT ["/usr/bin/autossh", "-M", "0", "-i", "/ssh_identity",
"-oServerAliveInterval=30", "-oServerAliveCountMax=3", "-T", "-N",
"-oStrictHostKeyChecking=no", "-oUserKnownHostsFile=/dev/null", "-L"]  

