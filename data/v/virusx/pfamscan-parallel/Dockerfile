FROM virusx/pfamscan:1.6  
COPY pfamscan-parallel.sh /usr/local/bin/  
RUN apt-get update && \  
apt-get install -y parallel && \  
chmod +x /usr/local/bin/pfamscan-parallel.sh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

