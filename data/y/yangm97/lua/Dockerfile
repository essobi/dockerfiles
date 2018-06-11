FROM alpine:3.6  
ENTRYPOINT ["lua"]  
  
ARG LUA_VERSION=5.1  
RUN apk add --no-cache lua${LUA_VERSION} lua${LUA_VERSION}-dev build-base git
bash unzip curl openssl-dev && \  
ln -s /usr/bin/lua${LUA_VERSION} /usr/local/bin/lua && \  
cd /tmp && \  
git clone https://github.com/keplerproject/luarocks.git && \  
cd luarocks && \  
sh ./configure --lua-version=${LUA_VERSION} && \  
make build install && \  
rm -rf /tmp/*  

