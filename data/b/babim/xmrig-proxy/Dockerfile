FROM babim/ubuntubase  
RUN apt-get update && apt-get install -y git build-essential cmake libuv1-dev
uuid-dev libmicrohttpd-dev  
RUN git clone https://github.com/xmrig/xmrig-proxy.git && mv xmrig-proxy
xmrig-proxy-dev && \  
cd xmrig-proxy-dev && mkdir build && cd build && \  
cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib/x86_64-linux-
gnu/libuv.a && \  
make && mv xmrig-proxy / && cd ../../ && rm -rf xmrig-proxy-dev  
RUN apt-get purge -y git build-essential cmake && rm -rf /var/lib/apt/lists/**  
WORKDIR /  
ENTRYPOINT ["./xmrig-proxy", "--donate-level=1"]  

