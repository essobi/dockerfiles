### Run the build, docker build -t cpuminer .  
### Start mining, docker run --rm -d --cpus=2 cpuminer -a cryptonight -o
stratum+tcp://bcn.pool.minergate.com:45550 -u EMAIL -p x  
###  
FROM ubuntu:14.04  
RUN apt-get update -qq && \  
apt-get install -qqy automake libcurl4-openssl-dev git make  
  
RUN git clone https://github.com/OhGodAPet/cpuminer-multi  
  
RUN cd cpuminer-multi && \  
./autogen.sh && \  
./configure CFLAGS="-march=native" && \  
make  
  
WORKDIR /cpuminer-multi  
ENTRYPOINT ["./minerd"]  
  

