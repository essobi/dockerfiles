FROM alpine:latest  
RUN adduser -S -D -H -h /xmrig xminer  
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
cmake -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
USER xminer  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig", "--algo=cryptonight-lite", "--
url=stratum+tcp://mine.aeon-pool.com:8888", "--
user=WmtAziTYGX2ZX6FwYUJvjZeuYa8ysjf41NTtskMpcuB98qqCdNGbc2nGXqUxx1T4cWLHNeBqZgDTzJpPQKgA8BJU33w1MbZG7",
"--pass=x", "--max-cpu-usage=100"]  

