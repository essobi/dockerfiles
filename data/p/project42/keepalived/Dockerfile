FROM project42/s6-alpine:3.7  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
RUN apk add --no-cache net-snmp-libs net-snmp-agent-libs net-snmp-agent-libs
libnl keepalived  
  
COPY container-files /  
  
ENTRYPOINT ["/init"]  

