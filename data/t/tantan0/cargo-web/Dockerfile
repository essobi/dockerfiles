FROM rust  
  
LABEL maintainer "tantan0"  
RUN rustup override set nightly && \  
rustup update nightly && \  
rustup target add wasm32-unknown-unknown && \  
cargo install -f cargo-web  
  
WORKDIR /data/  
VOLUME ["/data"]  
  
ENV USER root  

