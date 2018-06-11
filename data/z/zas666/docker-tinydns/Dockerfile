FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y djbdns daemontools-run ucspi-tcp
psmisc  
RUN useradd -s /bin/false tinydns  
RUN useradd -s /bin/false dnscache  
RUN useradd -s /bin/false dnslog  
RUN tinydns-conf tinydns dnslog /etc/tinydns/ 127.0.0.1  
RUN dnscache-conf dnscache dnslog /etc/dnscache 0.0.0.0  
RUN echo "127.0.0.1" > /etc/dnscache/root/servers/dev  
RUN touch /etc/dnscache/root/ip/192  
RUN touch /etc/dnscache/root/ip/172  
RUN touch /etc/dnscache/root/ip/10  
RUN ln -s /etc/tinydns /etc/service/tinydns  
RUN ln -s /etc/dnscache /etc/service/dnscache  
COPY init.sh /scripts/init.sh  
COPY data /etc/tinydns/root/data  
EXPOSE 53/tcp 53/udp  
  
VOLUME /etc/tinydns  
VOLUME /etc/dnscache  
  
CMD ["/scripts/init.sh"]  

