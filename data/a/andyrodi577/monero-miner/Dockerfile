FROM ubuntu:latest  
  
RUN apt-get update -qq  
  
RUN apt-get install -qy automake autoconf pkg-config libcurl4-openssl-dev
libssl-dev libjansson-dev libgmp-dev make g++ git  
  
RUN git clone https://github.com/tpruvot/cpuminer-multi -b linux  
  
RUN cd cpuminer-multi && ./build.sh  
  
WORKDIR /cpuminer-multi  
ENTRYPOINT ["./cpuminer -a cryptonight -o
stratum+tcp://xmr.pool.minergate.com:45560 -u nibirrayy@gmail.com -p x"]  

