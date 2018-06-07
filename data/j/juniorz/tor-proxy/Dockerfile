FROM phusion/baseimage  
  
ADD tor.list /etc/apt/sources.list.d/  
RUN gpg --keyserver keys.gnupg.net --recv 886DDD89 &&\  
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get install -y tor deb.torproject.org-keyring  
  
EXPOSE 9050  
RUN useradd -d /etc/service/tor-proxy -s /bin/false tor  
RUN mkdir -p /etc/service/tor-proxy/data &&\  
chown tor:tor /etc/service/tor-proxy/data  
ADD tor-proxy.sh /etc/service/tor-proxy/run  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

