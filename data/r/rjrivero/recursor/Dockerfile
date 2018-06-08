FROM krallin/ubuntu-tini:trusty  
  
# Install pdns-recursor  
# Settings are stored at /etc/powerdns/recursor.conf  
RUN apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
pdns-recursor dnsutils && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose DNS ports  
EXPOSE 53 53/udp  
  
# Run pdns recursor  
CMD ["/usr/sbin/pdns_recursor", "--setuid=pdns", "--setgid=pdns", "--
daemon=no", "--local-address=0.0.0.0", "--local-port=53"]  

