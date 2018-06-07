FROM ubuntu:xenial  
MAINTAINER Nick Thieling <nick@adrift.io>  
  
# Json-RPC and P2P ports respectively. Open only 8333 externally.  
EXPOSE 8332  
EXPOSE 8333  
VOLUME /root/.bitcoin/  
  
# https://bitcoin.org/en/full-node  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:bitcoin/bitcoin -y  
RUN apt-get update -y # update index after ppa add  
# install bitcoind and configuration  
RUN apt-get install bitcoind -y  
  
ENTRYPOINT [ "bitcoind" ]  

