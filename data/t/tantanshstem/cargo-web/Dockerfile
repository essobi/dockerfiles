FROM rust  
  
LABEL maintainer ""  
RUN rustup override set nightly && \  
rustup update nightly && \  
rustup target add wasm32-unknown-unknown && \  
cargo install -f cargo-web  
  
WORKDIR /src/  
ENV USER root  

