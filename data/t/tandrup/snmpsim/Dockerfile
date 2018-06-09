FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils snmpsim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser --system snmpsim  
  
ADD data /usr/share/snmpsim/data  
  
EXPOSE 161/udp  
  
CMD snmpsimd --agent-udpv4-endpoint=0.0.0.0:161 --process-user=snmpsim
--process-group=nogroup $EXTRA_FLAGS  

