FROM counterparty/base  
  
MAINTAINER Monaparty Developers <dev@monaparty.me>  
  
# install monacoin-addrindex  
RUN apt-get update && apt-get upgrade -y && \  
add-apt-repository -y ppa:cryptcoin.junkey/monacoin-addrindex && apt-get
update && \  
apt-get install -y monacoind-addrindex  
  
# Set up bitcoind dirs and files  
RUN mkdir -p /root/.monacoin/  
COPY bitcoin.conf /root/.monacoin/monacoin.conf  
COPY start.sh /usr/local/bin/start.sh  
RUN chmod a+x /usr/local/bin/start.sh  
  
EXPOSE 9401 9402 19403 19402  
  
# NOTE: Defaults to running on mainnet, specify -e TESTNET=1 to start up on
testnet  
ENTRYPOINT ["start.sh"]  

