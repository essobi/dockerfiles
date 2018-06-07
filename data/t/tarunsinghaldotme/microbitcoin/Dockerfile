FROM ubuntu:latest  
  
LABEL "vendor"="Tarun Singhal"  
LABEL "vendor.url"="http://www.tarunsinghal.me"  
LABEL "maintainer"="hello@tarunsinghal.me"  
  
RUN apt-get update -y && apt-get install wget -y && apt-get install build-
essential libssl-dev libdb++-dev git libssl1.0.0-dbg libdb-dev libboost-all-
dev libminiupnpc-dev libevent-dev libcrypto++-dev libgmp3-dev -y  
  
WORKDIR /root/  
RUN git clone https://github.com/digixhub/MicroBitcoin.git  
  
WORKDIR /root/MicroBitcoin/src  
RUN mkdir -p obj/zerocoin  
  
RUN chmod +x leveldb/build_detect_platform  
RUN make -f makefile.unix RELEASE=1  
  
WORKDIR /root/.microbitcoin/  
  
EXPOSE 33013  
EXPOSE 33014  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

