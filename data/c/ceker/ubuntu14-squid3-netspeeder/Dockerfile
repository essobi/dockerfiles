FROM ubuntu:14.04.5  
MAINTAINER ceker "xsk.tehon.org"  
RUN apt-get update && \  
apt-get install -y libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev git
apache2-utils squid3 && \  
apt-get clean  
  
RUN mv /etc/squid3/squid.conf /etc/squid3/squid.conf.dist && \  
mkdir -p /var/cache/squid && \  
chown -R proxy:proxy /var/cache/squid  
ADD squid.conf /etc/squid3/squid.conf  
  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh && mv net_speeder /usr/local/bin/ &&
chmod +x /usr/local/bin/net_speeder  
  
EXPOSE 10101  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

