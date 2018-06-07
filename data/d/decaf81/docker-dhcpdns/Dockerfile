FROM debian:latest  
MAINTAINER decaf811 (decaf81@gmail.com)  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
VOLUME ["/etc/bind"]  
VOLUME ["/etc/dhcpd"]  
RUN apt-get -q -y update && apt-get -q -y -o "DPkg::Options::=--force-confold"
-o "DPkg::Options::=--force-confdef" install ipcalc dumb-init bind9 isc-dhcp-
server man procps supervisor psmisc dnsutils  
  
COPY dhcpd.conf /root/dhcpd.conf.template  
COPY entrypoint.sh /entrypoint.sh  
COPY zonefile.template /root/zonefile.template  
COPY named.conf.template /root/named.conf.template  
COPY rndc.conf.template /root/rndc.conf.template  
RUN /bin/chown root:root /entrypoint.sh  
RUN /bin/chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

