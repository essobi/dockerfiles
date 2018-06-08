FROM debian:stable  
MAINTAINER andreas@rammhold.de  
  
ENV RUSTUP_TOOLCHAIN="stable" \  
RUSTUP_HOME=/usr/local/rustup \  
CARGO_HOME=/usr/local/cargo \  
PATH=/usr/local/cargo/bin:$PATH  
  
# Install required debian packages  
RUN set -eux; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
dpkg-dev \  
file \  
g++ \  
gcc \  
libc6-dev \  
libssl-dev \  
make \  
patch \  
libtool \  
curl \  
ca-certificates \  
liblzma-dev \  
pkg-config \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain
${RUSTUP_TOOLCHAIN}; \  
rustup --version; \  
cargo --version; \  
rustc --version;  
  
RUN cargo install cargo-deb;

