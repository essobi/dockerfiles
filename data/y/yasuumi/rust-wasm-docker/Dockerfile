FROM ubuntu:16.04  
MAINTAINER "Yasuumi Nishikawa" <yasu.umi.19910101@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV PATH=/root/.cargo/bin:$PATH  
  
RUN apt-get update && apt-get upgrade -qy && \  
apt-get install -y \--no-install-recommends \  
curl git openssl libssl-dev ca-certificates \  
build-essential python && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \  
  
curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly -y && \  
rustup update && \  
rustup default nightly && \  
  
mkdir /emscripten && cd /emscripten && \  
curl -O https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-
portable.tar.gz && \  
tar -xzf emsdk-portable.tar.gz && cd ./emsdk-portable && \  
./emsdk update && ./emsdk install latest && ./emsdk activate && \  
/bin/bash ./emsdk_env.sh && ls -la && cat ./emsdk_set_env.sh >> /root/.profile
&& \  
  
rustup target add wasm32-unknown-emscripten  
  
CMD ["/bin/bash", "--login"]  

