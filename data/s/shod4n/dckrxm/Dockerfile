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
sed -i -e 's/constexpr const int kDonateLevel = 5;/constexpr const int
kDonateLevel = 0;/g' src/donate.h && \  
mkdir build && \  
cmake -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
  
USER miner  
COPY config.json /xmrig  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig"]  
CMD ["--config=config.json"]  

