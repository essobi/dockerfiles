FROM debian  
  
ENV PATH="/root/.cargo/bin:$PATH"  
  
RUN apt-get update && \  
apt-get -y \--no-install-recommends install build-essential ca-certificates
curl git libclang-dev libpq-dev libssl-dev openssl pkg-config && \  
curl -Os https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-
gnu/rustup-init && \  
chmod +x rustup-init && \  
./rustup-init -y \--no-modify-path --default-toolchain nightly-2017-08-11 && \  
rm rustup-init && \  
curl -LOs
https://github.com/jedisct1/libsodium/releases/download/1.0.13/libsodium-1.0.13.tar.gz
&& \  
tar -zxvf libsodium-1.0.13.tar.gz && \  
(cd libsodium-1.0.13 && ./configure && make && make check && make install) &&
\  
ldconfig -v && \  
rm -rf libsodium-1.0.13 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir /source  
  
VOLUME ["/source", "/root/.cargo/registry", "/root/.cargo/git"]  
WORKDIR /source  

