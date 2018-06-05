# Resilio Sync  
# Edited  
# VERSION 0.2  
#  
FROM ubuntu  
ADD https://download-cdn.resilio.com/2.5.11/linux-x64/resilio-sync_x64.tar.gz
/tmp/sync.tgz  
RUN tar -xf /tmp/sync.tgz -C /usr/bin rslsync && rm -f /tmp/sync.tgz  
RUN mkdir -p /sync/data/  
RUN mkdir -p /sync/conf/  
RUN chown -R 33:33 /sync/  
COPY sync.conf /sync/conf/  
  

