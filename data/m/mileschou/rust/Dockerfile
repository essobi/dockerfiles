FROM debian:jessie  
  
ENV BUILD_DEPS \  
ca-certificates \  
curl \  
file  
ENV PERSISTENT_DEPS \  
g++ \  
sudo  
  
RUN set -xe && \  
apt-get update -y && \  
apt-get install -y --no-install-recommends --no-install-suggests \  
$PERSISTENT_DEPS \  
$BUILD_DEPS \  
&& rm -r /var/lib/apt/lists/* && \  
curl -sSf https://static.rust-lang.org/rustup.sh | sh && \  
apt-get purge -y $BUILD_DEPS && \  
rustc --version  

