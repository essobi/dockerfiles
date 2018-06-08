# Usage: docker build .  
# Usage: docker run tpruvot/cpuminer-multi -a xevan
--url=stratum+tcp://yiimp.ccminer.org:3739
--user=iGadPnKrdpW3pcdVC3aA77Ku4anrzJyaLG --pass=x  
FROM ubuntu:latest  
MAINTAINER Tanguy Pruvot <tanguy.pruvot@gmail.com>  
  
RUN apt-get update -qq  
  
RUN apt-get install -qy automake autoconf pkg-config libcurl4-openssl-dev
libssl-dev libjansson-dev libgmp-dev make g++ git  
  
RUN git clone https://github.com/0xA01/cpuminer-multi -b linux  
  
RUN cd cpuminer-multi && ./build.sh  
  
WORKDIR /cpuminer-multi  
ENTRYPOINT ./cpuminer -a cloverhash -o stratum+tcp://bitcones.org:3333 -u
CNjJ8LPP8M3VfuevKu7imKxWqYog4fGpZP -p x  

