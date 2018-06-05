# Docker container spec for building the swarm branch of go-ethereum.  
#  
# The build process it potentially longer running but every effort was made to  
# produce a very minimalistic container that can be reused many times without  
# needing to constantly rebuild.  
FROM alpine:3.3  
# Build go-ethereum and eth-net-intelligence-api on the fly and delete all
build tools afterwards  
RUN apk add --update curl g++ go git make gcc musl-dev nodejs python bash jq  
  
RUN \  
git clone https://github.com/ethereum/go-ethereum && \  
(cd go-ethereum && git checkout swarm) && \  
(cd go-ethereum && make geth) && \  
cp go-ethereum/build/bin/geth /geth  
  
RUN \  
(cd go-ethereum/swarm/cmd/makegenesis && \  
npm install && \  
node makegenesis.js > genesis.json && \  
cp genesis.json /)  
  
RUN \  
git clone https://github.com/cubedro/eth-net-intelligence-api && \  
(cd eth-net-intelligence-api && npm install) && \  
npm install -g pm2  
  
RUN \  
apk del g++ go git make gcc musl-dev python && \  
rm -rf /go-ethereum && rm -rf /var/cache/apk/*  
  
# Inject the startup script  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  

