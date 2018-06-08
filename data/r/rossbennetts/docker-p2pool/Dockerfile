# Dockerfile for P2Pool Server  
# http://p2pool.in/  
FROM alpine  
MAINTAINER rossbennetts <ross.bennetts@gmail.com>  
LABEL description="Dockerised P2Pool"  
  
RUN apk --no-cache add \  
git \  
perl \  
python \  
python-dev \  
py-twisted \  
gcc \  
g++  
  
WORKDIR /p2pool  
ENV P2POOL_HOME /p2pool/p2pool  
ENV P2POOL_REPO https://github.com/forrestv/p2pool  
  
RUN git clone -b master $P2POOL_REPO $P2POOL_HOME  
  
WORKDIR $P2POOL_HOME  
RUN git submodule init \  
&& git submodule update  
  
# Remove to reduce size  
RUN apk -v del \  
git \  
python-dev \  
perl \  
gcc \  
g++  
  
EXPOSE 9332 9333  
ENV BITCOIND_RPCUSER bitcoinrpc  
ENV BITCOIND_RPCPASSWORD 4C3NET7icz9zNE3CY1X8eSVrtpnSb6KcjEgMJW3armRV  
ENV BITCOIND_RPCHOST 192.168.99.1  
ENV BITCOIND_RPCPORT 8332  
ENV BITCOIND_P2PPORT 8333  
ENV P2POOL_FEE 0  
ENV P2POOL_DONATION 0  
ENV BTC_ADDRESS 1KwmPhzawgCgLFgzpvW6rSkzRiLRbWNSKh  
  
# Default arguments, can be overriden  
WORKDIR $P2POOL_HOME  
CMD python run_p2pool.py \  
\--give-author $P2POOL_DONATION \  
-f $P2POOL_FEE \  
-a $BTC_ADDRESS \  
\--bitcoind-address $BITCOIND_RPCHOST \  
\--bitcoind-rpc-port $BITCOIND_RPCPORT \  
\--bitcoind-p2p-port $BITCOIND_P2PPORT \  
$BITCOIND_RPCUSER $BITCOIND_RPCPASSWORD  
  
# End.  

