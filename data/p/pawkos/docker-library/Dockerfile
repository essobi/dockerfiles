FROM ubuntu:trusty  
# Syncthing-Relay Server  
MAINTAINER Blake VandeMerwe <blakev@null.net>  
  
ENV DEBUG false  
ENV SERV_PORT 22067  
# 10 mbps  
ENV RATE_GLOBAL 10000000  
# 500 kbps  
ENV RATE_SESSION 500000  
ENV TIMEOUT_MSG 1m45s  
ENV TIMEOUT_NET 3m30s  
ENV PING_INT 1m15s  
  
ENV PUBLIC_IP "0.0.0.0"  
ENV PROVIDED_BY "syncthing-relay docker container"  
RUN apt-get update && apt-get install ca-certificates -y  
ADD https://github.com/syncthing/relaysrv/releases/download/v0.12.1/relaysrv-
linux-amd64.tar.gz /tmp/relaysrv.tar.gz  
RUN tar -xzvf /tmp/relaysrv.tar.gz && rm /tmp/relaysrv.tar.gz && mv relaysrv*
/srv/relaysrv  
  
EXPOSE 22070 ${SERV_PORT}  
  
CMD /srv/relaysrv/relaysrv \  
-keys="/srv/relaysrv" \  
-listen="${PUBLIC_IP}:${SERV_PORT}" \  
-debug="${DEBUG}" \  
-global-rate="${RATE_GLOBAL}" \  
-per-session-rate="${RATE_SESSION}" \  
-message-timeout="${TIMEOUT_MSG}" \  
-network-timeout="${TIMEOUT_NET}" \  
-ping-interval="${PING_INT}" \  
-provided-by="${PROVIDED_BY}" \  
-pools=""  

