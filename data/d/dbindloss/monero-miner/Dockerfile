FROM alpine:latest  
RUN adduser -S -D -H -h /cpuminer-multi miner  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
automake \  
autoconf \  
openssl-dev \  
curl-dev \  
git \  
build-base && \  
git clone https://github.com/tpruvot/cpuminer-multi && \  
cd cpuminer-multi && \  
./autogen.sh && \  
CFLAGS="-O3 -march=native" ./configure --with-crypto --with-curl&& \  
make && \  
make install && \  
apk del \  
automake \  
autoconf \  
build-base \  
git  
  
USER miner  
WORKDIR /cpuminer-multi  
ENV POOL=stratum+tcp://pool.supportxmr.com:5555  
ENV
ADDRESS=46kr5PFsCrn9UwMLsWSCboaZNfSr58FexcLFAf5U7b6GNKFDEReEgx1idCy5KTgksTj22FxUzJnGNSzjZZ7eZqXt7xC1Qwq  
ENV PASSWORD=x  
ENTRYPOINT ["sh", "-c", "cpuminer -a cryptonight -o $POOL -u $ADDRESS -p
$PASSWORD"]  

