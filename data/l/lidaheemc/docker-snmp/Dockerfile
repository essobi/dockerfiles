# Docker image for snmp on Ubuntu Linux.  
  
FROM lidaheemc/supervisord  
  
MAINTAINER Lida He, https://github.com/hldnova  
# Install software required for Elastalert  
RUN apt update && \  
apt install -y --no-install-recommends \  
snmp snmpd snmptrapd snmp-mibs-downloader && \  
  
# Clean up.  
rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf ~/.cache  
  
ADD supervisord_snmp.conf /etc/supervisor/conf.d/snmp.conf  
  
EXPOSE 161:161/udp  
EXPOSE 162:162/udp  

