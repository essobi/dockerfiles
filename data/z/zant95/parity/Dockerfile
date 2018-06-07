FROM ubuntu:16.04  
WORKDIR /tmp/parity  
  
ARG BUILD_TAG  
ENV BUILD_TAG ${BUILD_TAG:-stable}  
  
ENV RUNTIME_PACKAGES openssl  
ENV BUILD_PACKAGES build-essential file pkg-config libssl-dev libudev-dev curl
ca-certificates git  
  
RUN echo "Building from '${BUILD_TAG}' tag" && \  
# Install tools and dependencies  
apt-get update && \  
apt-get install --assume-yes \--no-install-recommends $RUNTIME_PACKAGES
$BUILD_PACKAGES && \  
# Install Rust  
curl "https://sh.rustup.rs" -sSf | sh -s -- -y && \  
PATH="/root/.cargo/bin:$PATH" && \  
RUST_BACKTRACE="1" && \  
# Build Parity  
git clone --recursive "https://github.com/ethcore/parity" . && \  
git checkout "$BUILD_TAG" && \  
git pull && \  
cargo build --release --features final && \  
strip target/release/parity && \  
file target/release/parity && \  
mv target/release/parity /usr/bin/parity && \  
# Cleanup  
apt-get purge --assume-yes \--auto-remove $BUILD_PACKAGES && \  
rm -rf /tmp/parity /root/.cargo /root/.multirust /root/.rustup  
  
EXPOSE 8080 8545 8180  
ENTRYPOINT ["/usr/bin/parity"]  

