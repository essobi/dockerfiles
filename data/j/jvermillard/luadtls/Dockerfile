FROM debian:7.4  
MAINTAINER jvermillard@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y git cmake build-essential lua5.1 lua-socket
liblua5.1-0-dev autoconf  
RUN mkdir -p /build && cd /build && git clone
https://github.com/sbernard31/luadtls --recursive && mkdir luadtls/build && cd
luadtls/build  
RUN cd /build/luadtls/build && cmake .. && make  
RUN ls -alh /build/luadtls/build  
ENV LUA_PATH /build/luadtls/build/?/init.lua;;  

