FROM ubuntu:14.04  
MAINTAINER Åsmund Kamphaug  
  
RUN apt-get update -qq  
  
RUN apt-get install -qy automake autoconf pkg-config libcurl4-openssl-dev
libssl-dev libjansson-dev libgmp-dev make g++ git  
  
RUN git clone https://github.com/tpruvot/cpuminer-multi -b linux  
  
RUN cd cpuminer-multi && ./build.sh  
  
WORKDIR /cpuminer-multi  
#ENTRYPOINT ["./cpuminer","-a", "cryptonight","-o", "stratum+tcp://xmr-
eu.suprnova.cc:5222"]  
ENTRYPOINT ./cpuminer -a cryptonight -o stratum+tcp://xmr-eu.suprnova.cc:5222
-u Ozzykampha.worker2 -p passord  

