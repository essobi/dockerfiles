FROM ubuntu  
MAINTAINER Enrique Vicent  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y -qq upgrade && \  
apt-get -y -qq install git-all build-essential nodejs vim curl parallel
language-pack-en && \  
apt-get -y -qq install software-properties-common && \  
add-apt-repository ppa:ethereum/ethereum && \  
add-apt-repository ppa:ethereum/ethereum-dev && \  
apt-get update && \  
apt-get -y -qq install geth solc ethereum && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone http://github.com/SilentCicero/meteor-dapp-cosmo.git  
WORKDIR /meteor-dapp-cosmo/app  
RUN curl https://install.meteor.com/ | sh  
RUN meteor update  
  
# creating an account  
RUN echo password > passwordfile ; geth --password passwordfile account new  
  
# generating dag file  
RUN mkdir /root/.ethash; geth --password passwordfile --rpc
--rpcaddr="localhost" \--unlock=0 --rpcport="8080"
\--rpccorsdomain="http://localhost:3000" \--maxpeers=0 makedag 0 /root/.ethash  
  
EXPOSE 8545  
EXPOSE 30303  
EXPOSE 3000  
CMD (echo "geth --password passwordfile --rpc --rpcaddr=\"localhost\" --mine
--unlock=0 --rpcport=\"8080\" --rpccorsdomain=\"http://localhost:3000\"
--maxpeers=0" ; echo "meteor run --port 0.0.0.0:3000") | parallel  
# docker build -t sede . && docker run --rm -ti -p 3000:3000 -p 8080:8080 sede
/bin/bash  

