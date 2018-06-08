FROM debian:wheezy  
MAINTAINER Bassam Tabbara <bassam.tabbara@quantum.com>  
  
RUN \  
echo deb http://http.debian.net/debian wheezy-backports main | tee
/etc/apt/sources.list.d/backports.list; \  
apt-get update; \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
wget \  
dnsmasq \  
syslinux \  
\--no-install-recommends; \  
rm -rf /var/lib/apt/lists/*  
  
# TODO: persist leases in /var/lib/misc/dnsmasq.leases /var/db/dnsmasq.leases  
VOLUME /hyve/boot  
  
ADD dnsmasq-run.sh dnsmasq-run.sh  
  
EXPOSE 53 53/udp 67 67/udp 68 68/udp 69/udp 4011/udp  
  
CMD [ "/dnsmasq-run.sh" ]  
  

