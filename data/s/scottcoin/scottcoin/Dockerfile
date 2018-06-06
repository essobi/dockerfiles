FROM alpine:3.3  
MAINTAINER "scottcoin"  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup -S scottcoin && adduser -S -G scottcoin scottcoin  
  
# Load dependencies  
RUN apk add --update-cache bash \  
curl \  
sudo \  
boost \  
openssl \  
protobuf \  
boost-program_options \  
db \  
db-c++ \  
libevent-dev \  
zeromq-dev \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /home/scottcoin/  
  
COPY scripts/* ./  
RUN chown scottcoin:scottcoin *  
RUN ./build.sh  
  
# Create config volume with appropriate permissions  
RUN mkdir .bitcoin && chown scottcoin:scottcoin .bitcoin  
# Use absolute path to avoid problems binding containers  
VOLUME /home/scottcoin/.bitcoin  
  
# Expose ports for bitcoin  
EXPOSE 8100  
EXPOSE 8101  
# Setup environment variables with appropriate defaults  
# MINTING_REWARD must match bitcoind's minting reward  
ENV CERTIFICATE_URL="http://scottlogic.github.io/scottcoin/key"\  
RPC_USER=scottnet \  
RPC_PASS=password \  
RPC_PORT=8101 \  
ADDRESS_SEED=139.59.196.66:8100 \  
CONNECT_TO="" \  
CERTIFICATE_POLL_DELAY=600 \  
MINTING_REWARD=1 \  
BURN_ADDRESS=1111111111111111111114oLvT2  
  
USER scottcoin  
  
ENTRYPOINT ["./launch.sh"]  

