FROM ubuntu:14.04  
## Install djbdns  
RUN apt-get update && \  
apt-get install daemontools daemontools-run ucspi-tcp djbdns -y  
  
## Configure tinydns  
# users  
RUN useradd -s /bin/false tinydns && \  
useradd -s /bin/false axfrdns && \  
useradd -s /bin/false dnslog  
# config dir and service  
RUN tinydns-conf tinydns dnslog /etc/tinydns 0.0.0.0 && \  
ln -s /etc/tinydns /etc/service/tinydns  
# symlink tinydns data file to /data/tinydns.data (volume mountpoint)  
RUN rm /etc/tinydns/root/data && \  
ln -s /data/tinydns.data /etc/tinydns/root/data  
  
## Configure axfrdns  
# config dir and service  
RUN axfrdns-conf axfrdns dnslog /etc/axfrdns /etc/tinydns 0.0.0.0 && \  
ln -s /etc/axfrdns /etc/service/axfrdns  
# symlink axfr tcp file to /data/axfrdns.tcp (volume mountpoint)  
RUN rm /etc/axfrdns/tcp && \  
ln -s /data/axfrdns.tcp /etc/axfrdns/tcp  
  
## Container addons scripts  
ADD ./rebuild_tinydns-data.sh /rebuild_tinydns-data.sh  
ADD ./rebuild_axfrdns-tcp.sh /rebuild_axfrdns-tcp.sh  
ADD ./init.sh /init.sh  
RUN chmod u+x /rebuild_tinydns-data.sh && \  
chmod u+x /rebuild_axfrdns-tcp.sh && \  
chmod u+x /init.sh  
  
## Docker config  
EXPOSE 53/udp  
EXPOSE 53  
CMD ["/init.sh"]

