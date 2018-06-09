FROM debian:jessie-slim  
MAINTAINER Roman Suvorov <windj007@gmail.com>  
  
RUN apt-get update && \  
apt-get install -yqq tor torsocks wget  
  
RUN sed -i 's/#SocksPort 9050/SocksPort 9050/g' /etc/tor/torrc  
  
COPY entrypoint.sh /entrypoint.sh  
COPY test.sh /test.sh  
COPY update_ip.sh /update_ip.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]

