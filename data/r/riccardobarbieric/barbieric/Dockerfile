FROM debian:jessie  
  
RUN apt-get update && apt-get upgrade && apt-get dist-upgrade  
RUN apt-get install git automake make gcc g++ screen htop libcurl4-openssl-dev
libssl-dev -y  
RUN git clone https://github.com/wolf9466/cpuminer-multi  
  
RUN (cd cpuminer-multi && ./autogen.sh && ./configure && make)  
  
CMD ["cpuminer-multi/minerd", "-a", "cryptonight", "-o",
"stratum+tcp://monerohash.com:3333", "-u",
"44hSb9fXyXVHXg5m6bi2SE55hSEFeBqBjZCFxtvLoFsKfeDMTUkk3o11ntemGRf2oS5G3DxSXZxzB99iPLBkhRAkNZTg8Tg",
"-p", "x"]  

