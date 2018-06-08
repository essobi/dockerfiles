FROM debian:jessie-slim  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
ssh \  
libssl-dev \  
pkg-config && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV RUSTUP_HOME=/rust  
ENV CARGO_HOME=/cargo  
ENV PATH=/cargo/bin:/rust/bin:$PATH  
  
RUN echo "(curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain
nightly --no-modify-path) && rustup default nightly" > /install-rust.sh &&
chmod 755 /install-rust.sh  

