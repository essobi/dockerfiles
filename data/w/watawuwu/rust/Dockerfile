# ref https://hub.docker.com/r/ekidd/rust-musl-builder/~/dockerfile/  
FROM ubuntu:16.04  
ARG TOOLCHAIN=stable  
ARG TARGET=x86_64-unknown-linux-musl  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
cmake \  
curl \  
file \  
git \  
musl-dev \  
musl-tools \  
libssl-dev \  
pkgconf \  
sudo \  
xutils-dev \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV PATH=/root/.cargo/bin:/usr/local/musl/bin:/usr/local/bin:/usr/bin:/bin  
  
RUN curl https://sh.rustup.rs -sSf | \  
sh -s -- -y --default-toolchain $TOOLCHAIN && \  
rustup default $TOOLCHAIN && \  
rustup target add $TARGET  
  
ADD cargo-config.toml /root/.cargo/config  
  
WORKDIR /root/libs  
  
RUN echo "Building OpenSSL" && \  
VERS=1.0.2l && \  
curl -O https://www.openssl.org/source/openssl-$VERS.tar.gz && \  
tar xvzf openssl-$VERS.tar.gz && cd openssl-$VERS && \  
env CC=musl-gcc ./Configure no-shared no-zlib -fPIC --prefix=/usr/local/musl
linux-x86_64 && \  
env C_INCLUDE_PATH=/usr/local/musl/include/ make depend && \  
make && sudo make install && \  
cd .. && rm -rf openssl-$VERS.tar.gz openssl-$VERS && \  
echo "Building zlib" && \  
VERS=1.2.11 && \  
cd /root/libs && \  
curl -LO http://zlib.net/zlib-$VERS.tar.gz && \  
tar xzf zlib-$VERS.tar.gz && cd zlib-$VERS && \  
CC=musl-gcc ./configure --static --prefix=/usr/local/musl && \  
make && sudo make install && \  
cd .. && rm -rf zlib-$VERS.tar.gz zlib-$VERS  
  
ENV OPENSSL_DIR=/usr/local/musl/ \  
OPENSSL_INCLUDE_DIR=/usr/local/musl/include/ \  
DEP_OPENSSL_INCLUDE=/usr/local/musl/include/ \  
OPENSSL_LIB_DIR=/usr/local/musl/lib/ \  
OPENSSL_STATIC=1 \  
PKG_CONFIG_ALLOW_CROSS=true \  
PKG_CONFIG_ALL_STATIC=true  
  
WORKDIR /app  

