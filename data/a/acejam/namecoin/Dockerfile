FROM ubuntu:14.04  
MAINTAINER Joshua Noble <acejam@gmail.com>  
  
ENV RPC_USER namecoinrpc  
ENV RPC_PASS P@ssw0rd  
ENV RPC_ALLOW_IP 127.0.0.1  
ENV MAX_CONNECTIONS 15  
ENV RPC_PORT 8336  
ENV PORT 8334  
RUN apt-get update && \  
apt-get install -y wget && \  
wget
http://download.opensuse.org/repositories/home:p_conrad:coins/xUbuntu_14.04/Release.key
&& \  
apt-key add - < Release.key && \  
echo "deb
http://download.opensuse.org/repositories/home:/p_conrad:/coins/xUbuntu_14.04/
/" > /etc/apt/sources.list.d/namecoin.list && \  
apt-get update && \  
apt-get install -y namecoin && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8336 8334  
VOLUME ["/data/namecoin"]  
CMD ["/usr/bin/namecoind", "-datadir=/data/namecoin"]  

