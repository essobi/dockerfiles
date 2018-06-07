FROM alpine:latest  
RUN adduser -S -D -H -h /xmrig miner  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
git \  
cmake \  
libuv-dev \  
build-base && \  
git clone https://github.com/xmrig/xmrig && \  
cd xmrig && \  
sed -i "s/kDefaultDonateLevel = 5/kDefaultDonateLevel = 0/g" src/donate.h && \  
sed -i "s/kMinimumDonateLevel = 1/kMinimumDonateLevel = 0/g" src/donate.h && \  
mkdir build && \  
cmake -DWITH_AEON=OFF -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
USER miner  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig","-o","pool.t00ls.ru:443","--safe","-k"]  

