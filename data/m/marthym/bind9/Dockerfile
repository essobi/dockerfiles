FROM debian:latest  
  
# Install Server  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -y update && \  
apt-get -y install bind9  
  
# Configure  
RUN echo "include \"/etc/bind/example.local.conf\";" >>
/etc/bind/named.conf.local  
ADD conf/bind /etc/bind  
  
# Install Service  
ADD services /etc/sv  
  
EXPOSE 53  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

