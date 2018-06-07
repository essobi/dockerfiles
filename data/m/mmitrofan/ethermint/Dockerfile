FROM golang:1.9.2  
ARG ETHERMINT_VERSION=0.5.3  
ARG TENDERMINT_VERSION=0.15.0  
ARG GETH_VERSION=1.7.3  
# Install pre-requisites  
RUN apt-get update && apt-get install -y zip unzip curl apt-transport-https jq  
  
# Add ethermint app  
ADD
https://github.com/tendermint/ethermint/releases/download/v${ETHERMINT_VERSION}/ethermint_${ETHERMINT_VERSION}_linux-
amd64.zip /tmp/ethermint.zip  
  
# Add tendermint app  
ADD
https://github.com/tendermint/tendermint/releases/download/v${TENDERMINT_VERSION}/tendermint_${TENDERMINT_VERSION}_linux_amd64.zip
/tmp/tendermint.zip  
  
# Add geth app  
ADD https://github.com/ethereum/go-ethereum/archive/v${GETH_VERSION}.zip
/tmp/geth.zip  
  
# Finish install  
WORKDIR /tmp  
RUN unzip /tmp/ethermint.zip && mv ethermint /usr/local/bin/ && \  
unzip /tmp/tendermint.zip && mv tendermint /usr/local/bin/ && \  
unzip /tmp/geth.zip && cd go-ethereum-${GETH_VERSION} && make geth && mv
/tmp/go-ethereum-${GETH_VERSION}/build/bin/geth /usr/local/bin/  
  
# Install eth-net-intelligence-api  
WORKDIR /  
RUN git clone https://github.com/cubedro/eth-net-intelligence-api && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && apt-get install -y nodejs && \  
cd /eth-net-intelligence-api && \  
npm install && npm install -g pm2  
  
EXPOSE 46656 46657 8545 8546 30303 30303/udp 30301/udp  
  
CMD ["ethermint"]  

