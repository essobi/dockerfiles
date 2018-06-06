# Usage: docker build .  
# Usage: docker run rbrayner/cryptonight -a cryptonight -a cryptonight -o
stratum+tcp://cryptonight.usa.nicehash.com:3355 -u account.worker1  
FROM ubuntu:14.04  
MAINTAINER Rodrigo Brayner <rbrayner@gmail.com>  
  
RUN apt-get update -qq  
  
RUN apt-get install -qy automake autoconf pkg-config libcurl4-openssl-dev
libssl-dev libjansson-dev libgmp-dev make g++ git  
  
RUN git clone https://github.com/tpruvot/cpuminer-multi -b linux  
  
COPY build.sh /cpuminer-multi/  
  
RUN chmod +x /cpuminer-multi/build.sh  
  
#RUN cd cpuminer-multi  
RUN cd cpuminer-multi && ./build.sh  
  
WORKDIR /cpuminer-multi  
  
ENTRYPOINT ["./cpuminer"]  
  

