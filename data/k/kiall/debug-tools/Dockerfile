FROM ubuntu:16.04  
RUN apt-get update && apt-get install --yes --force-yes iputils-ping curl wget
net-tools dnsutils netcat-openbsd postgresql-client mysql-client  
  
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"  

