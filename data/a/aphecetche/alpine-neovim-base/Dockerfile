FROM alpine:3.3  
  
MAINTAINER Laurent Aphecetche <laurent.aphecetche@gmail.com>  
  
ENV CMAKE_EXTRA_FLAGS=-DENABLE_JEMALLOC=OFF  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update-cache --virtual build-deps --no-cache \  
autoconf \  
automake \  
cmake \  
g++ \  
git \  
libtool \  
libuv \  
linux-headers \  
lua5.3-dev \  
m4 \  
make \  
unzip \  
libtermkey-dev \  
lua-sec \  
&& \  
apk add --update-cache \  
libtermkey \  
unibilium && \  
git clone --depth=1 https://github.com/neovim/libvterm.git && \  
cd libvterm && \  
make && \  
make install && \  
cd ../ && rm -rf libvterm && \  
git clone --depth=1 https://github.com/neovim/neovim.git nvim && \  
cd nvim && \  
make && \  
make install && \  
cd .. && \  
rm -rf nvim && \  
apk del build-deps  
  
ENTRYPOINT /usr/local/bin/nvim  
  

