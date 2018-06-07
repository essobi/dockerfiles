# Pull base image.  
FROM ubuntu  
  
RUN \  
sed -ri 's/\/archive\\.ubuntu\\.com/\/kr\\.archive\\.ubuntu\\.com/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y open-vm-tools && \  
rm -rf /var/lib/apt/lists/*  
  
COPY files/init.sh /  
# Define default command.  
CMD ["/init.sh"]  

