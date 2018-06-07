FROM memcached:1.4  
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-
alerts@googlegroups.com>  
  
# Install Chaperone  
USER root  
RUN \  
apt-get update && \  
apt-get upgrade -y libc6 && \  
apt-get install -y --no-install-recommends python3-pip && \  
pip3 install chaperone && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/*  
  
# Chaperone setup  
COPY chaperone.conf /etc/chaperone.d/chaperone.conf  
  
USER memcache  
ENTRYPOINT ["/usr/local/bin/chaperone"]  
CMD ["--user", "memcache"]  

