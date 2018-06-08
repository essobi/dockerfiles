FROM alpine:latest  
RUN adduser -S -D -H -h /xmrig miner  
COPY . xmrig  
RUN apk --no-cache upgrade && \  
apk --no-cache add \  
cmake \  
libuv-dev \  
build-base && \  
cd xmrig && \  
mkdir build && \  
cmake -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apk del \  
build-base \  
cmake  
USER miner  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig"]

