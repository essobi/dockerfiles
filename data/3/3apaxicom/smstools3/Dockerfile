FROM ubuntu  
RUN apt-get update && apt-get install -y --force-yes build-essential manpages-
dev  
ADD http://smstools3.kekekasvi.com/packages/smstools3-3.1.21.tar.gz /tmp/  
RUN tar -xzf /tmp/smstools3-3.1.21.tar.gz -C /tmp; \  
cd /tmp/smstools3 && \  
make && make install && \  
mkdir -p /var/log/smstools/smsd_stats /var/run/smstools\  
cd && rm -rf /tmp/smstools3  
  
CMD ["smsd", "-t"]  

