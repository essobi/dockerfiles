FROM alpine:latest  
MAINTAINER Sean Johnson <sean.johnson@maio.me>  
  
# Version of Lua we're building the image for.  
ENV LUA_VERSION 5.1  
ENV LUA_PACKAGE lua${LUA_VERSION}  
  
# Update apk index.  
RUN apk update  
  
# Install packages necessary for Lua, Luarocks.  
RUN apk add ${LUA_PACKAGE}  
RUN apk add ${LUA_PACKAGE}-dev  
  
# Build dependencies.  
RUN apk add build-base git bash unzip  
  
# Build Luarocks.  
RUN cd /tmp && \  
git clone https://github.com/keplerproject/luarocks.git && \  
cd luarocks && \  
sh ./configure && \  
make build install && \  
cd && \  
rm -rf /tmp/luarocks  

