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
mkdir build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
USER miner  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig -o stratum+tcp://xmr-eu1.nanopool.org:14444 -u
49KZjKD9McXR9VpmcnWAczgRChyYckiXQVTtsnr8so84FA8ttpkvLrsKpmAHJ7vLUqHGT3sV2dneYBfqFu7kunBp4ARGRDc
-p x"]  

