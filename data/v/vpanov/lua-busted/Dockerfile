FROM alpine  
RUN \  
apk update && \  
apk add \  
ca-certificates \  
gcc \  
libqrencode \  
lua5.1 lua5.1-cjson lua5.1-dev lua5.1-libs lua5.1-sec lua5.1-socket \  
make musl-dev \  
openssl \  
perl \  
unzip \  
&& \  
\  
cd /tmp && \  
wget http://luarocks.org/releases/luarocks-2.3.0.tar.gz && \  
tar zxpf luarocks-2.3.0.tar.gz && \  
cd luarocks-2.3.0 && \  
./configure --prefix=/usr && \  
make bootstrap && \  
luarocks install bit32 && \  
luarocks install luaposix && \  
luarocks install busted && \  
\  
cd / && rm -rf /tmp/* && \  
\  
apk del \  
gcc \  
libc-utils \  
libgcc \  
libstdc++ \  
make mpc1 mpfr3 musl-dev musl-utils \  
perl \  
scanelf \  
&& \  
echo OK!  

