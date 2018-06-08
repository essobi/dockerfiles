FROM ubuntu:12.04  
RUN \  
apt-get update && \  
apt-get install -y build-essential libssl-dev libboost-all-dev git
libdb5.1-dev libdb5.1++-dev libminiupnpc-dev curl && \  
mkdir /tmp/litecoind && \  
curl -sL https://github.com/litecoin-project/litecoin/tarball/v0.8.4.1 | tar
zx -C /tmp/litecoind --strip-components=1 && \  
cd /tmp/litecoind/src && \  
make -j4 -f makefile.unix && \  
cp /tmp/litecoind/src/litecoind /usr/bin/litecoind && \  
rm -rf /tmp/litecoind  
EXPOSE 9332  
CMD ["/usr/bin/litecoind", "-datadir=/data", "--printtoconsole"]  
  

