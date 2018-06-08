FROM debian:stable  
MAINTAINER juzeon <master@skyju.cc>  
  
RUN apt-get update && \  
apt-get clean && \  
apt-get install -y openssh-server python python-pip python-m2crypto
libnet1-dev libpcap0.8-dev git gcc && \  
apt-get clean  
  
RUN git clone -b manyuser https://github.com/breakwa11/shadowsocks.git ssr  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
RUN mv net_speeder /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

