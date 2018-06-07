FROM ubuntu:16.04 AS BUILD  
RUN apt-get update && apt-get install -y git automake autoconf pkg-config
libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev make g++  
#cmake build-essential libboost-all-dev && apt-get clean && rm -rf
/var/lib/apt/lists/*  
WORKDIR /build  
RUN git clone \--depth 1 https://github.com/luisvasquez/cpuminer-easy.git && \  
cd cpuminer-easy/ && ./build-linux.sh  
RUN \  
cp /build/cpuminer-easy/cpuminer /usr/bin/cpuminer && \  
ldd /usr/bin/cpuminer | grep -Eo '/[^ ]+' > cpuminer.dep_ldd && \  
dpkg -S $(cat cpuminer.dep_ldd) | perl -pe's/:.*//' | sort -u >
cpuminer.dep_packages  
  
FROM ubuntu:16.04 AS MAIN  
COPY \--from=BUILD /usr/bin/cpuminer /usr/bin/  
COPY \--from=BUILD /build/cpuminer.dep_packages /  
RUN apt-get update && apt-get install -y inetutils-ping $(cat /*.dep_packages)
--no-install-recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /*.dep_packages  
ENV \  
ALGO=cryptonight \  
POOL= \  
USERNAME= \  
PASSWORD= \  
WALLET=361yTPdoXcBpWRJDpPJSoC2v5Ss3fYM3FL \  
WORKER=  
ADD bootstrap.sh bootstrap.sh  
ENTRYPOINT [ "./bootstrap.sh" ]  

