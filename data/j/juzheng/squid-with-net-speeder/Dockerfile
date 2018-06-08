FROM debian:wheezy  
MAINTAINER juzeon <master@skyju.cc>  
  
RUN apt-get update && \  
apt-get clean && \  
apt-get install -y curl squid openssh-server libnet1-dev libpcap0.8-dev git
gcc && \  
apt-get clean  
  
RUN echo "root:password"|chpasswd  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
RUN mv net_speeder /usr/local/bin/  
  
COPY entrypoint.sh /usr/local/bin/  
  
RUN rm -rf /etc/squid/squid.conf  
COPY squid.conf /etc/squid/  
RUN mkdir -p /var/cache/squid && \  
chmod -R 777 /var/cache/squid && \  
/etc/init.d/squid stop && \  
squid -z && \  
/etc/init.d/squid start  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
EXPOSE 25  
EXPOSE 22  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

