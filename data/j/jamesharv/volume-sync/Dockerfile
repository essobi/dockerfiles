FROM ubuntu:14.04  
RUN PACKAGES="\  
rsync \  
lsyncd \  
" && \  
apt-get update && \  
apt-get install -y $PACKAGES && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TARGET=/tgt  
ENV MAX_FILES=150000  
COPY entrypoint.sh /entrypoint.sh  
COPY lsyncd.lua /etc/lsyncd.lua  
  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

