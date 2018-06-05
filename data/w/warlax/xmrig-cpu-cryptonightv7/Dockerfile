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
sed -i
's/48edfHu7V9Z84YzzMa6fUueoELZ9ZRXq9VetWzYGzKt52XU5xvqgzYnDK9URnRoJMk1j8nLwEVsaSWJ4fhdUyZijBGUicoD/48TJMi3gCx7cpKrnM9TVmodLdUnGJfuPHJR3mMQVyCXeKoEHWSAqwypJa78MkXBgZ31Na26FdFUb4Lcwx53epQXh1u5Gw8J/g'
./src/net/strategies/DonateStrategy.cpp && \  
mkdir build && \  
cmake -DCMAKE_BUILD_TYPE=Release -DWITH_HTTPD=OFF . && \  
make && \  
apk del \  
build-base \  
cmake \  
git  
USER miner  
WORKDIR /xmrig  
ENTRYPOINT ["./xmrig"]  

