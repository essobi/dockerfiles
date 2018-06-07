FROM resin/armv7hf-debian-qemu  
  
RUN ["cross-build-start"]  
  
ENV USER root  
ENV RUST_VERSION=1.19.0  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
openssh-client \  
libssl-dev \  
pkg-config && \  
curl -sO https://static.rust-lang.org/rustup/dist/armv7-unknown-linux-
gnueabihf/rustup-init && \  
chmod +x rustup-init && \  
./rustup-init -y --default-toolchain $RUST_VERSION \--no-modify-path && \  
DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y curl && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \  
rm -rf \  
rustup-init \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* && \  
mkdir /source  
  
ENV PATH $PATH:/root/.cargo/bin  
WORKDIR /source  
CMD ["/bin/bash"]  
  
RUN ["cross-build-end"]  

