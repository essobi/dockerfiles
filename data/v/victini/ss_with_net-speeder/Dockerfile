# shadowsocks-net-speeder  
FROM ubuntu:16.04  
MAINTAINER Iniv  
RUN apt-get update && \  
apt-get install -y python-pip libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev
git  
  
RUN pip install git+https://github.com/shadowsocks/shadowsocks.git@master  
  
RUN git clone https://github.com/snooda/net-speeder.git net-speeder  
WORKDIR net-speeder  
RUN sh build.sh  
  
RUN mv net_speeder /usr/local/bin/  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/net_speeder  
  
ENV PORT 6323  
ENV PASSWORD 666323  
ENV METHOD aes-256-cfb  
RUN ssserver -p $PORT -k $PASSWORD -m $METHOD  
  
# Configure container to run as an executable  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

