# usage: docker run rmtodd618/bikercoin-cpuminer -a cryptonight -o
stratum+tcp://pool.bikercoin.org:3001 -u {BICADDRESS} -p x --threads={CPUS}  
FROM ubuntu:latest  
RUN apt-get update && \  
apt-get install build-essential screen automake m4 openssl libssl-dev git
libjson0 libjson0-dev libcurl4-openssl-dev autoconf python-software-properties
-y  
RUN git clone https://github.com/wolf9466/cpuminer-multi.git  
RUN cd cpuminer-multi && \  
./autogen.sh && \  
./configure CFLAGS="-march=native" && \  
make  
WORKDIR /cpuminer-multi  
ENTRYPOINT ["./minerd"]

