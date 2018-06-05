FROM ubuntu:latest  
ENV USER root  
ENV RUST_VERSION=1.20.0  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
openssl \  
pkg-config  
RUN curl -sO https://static.rust-
lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz && \  
tar -xzf rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz && \  
./rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh --without=rust-docs
&& \  
DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y curl && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \  
rm -rf \  
rust-$RUST_VERSION-x86_64-unknown-linux-gnu \  
rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* && \  
mkdir /source  
RUN cargo install rustfmt -j 8  
RUN cargo install cargo-watch -j 8  
ENV PATH="/root/.cargo/bin:$PATH"  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

