FROM ubuntu:xenial  
  
# Install Bitcoin via the official PPA  
RUN apt-get update -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:bitcoin/bitcoin && \  
apt-get update -y && \  
apt-get install -y bitcoind && \  
apt-get remove \--purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean  
  
VOLUME ["/root/.bitcoin"]  
EXPOSE 8333  
  
CMD bitcoind -printtoconsole  

