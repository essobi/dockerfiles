FROM ubuntu:16.04  
LABEL maintainer "Joshua Noble <acejam@gmail.com>"  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8842ce5e && \  
echo "deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu xenial main" >
/etc/apt/sources.list.d/bitcoin.list  
  
RUN apt-get update && \  
apt-get install -y bitcoind=0.15.1-xenial1 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8332 8333  
VOLUME ["/data/bitcoin"]  
CMD ["/usr/bin/bitcoind", "-datadir=/data/bitcoin"]  

