FROM gifnksm/emscripten-incoming:latest  
MAINTAINER gifnksm (makoto.nksm@gmail.com)  
  
ARG RUST_TOOLCHAIN=${RUST_TOOLCHAIN:-stable}  
  
ENV RUSTUP_HOME=/rustup \  
CARGO_HOME=/rustup \  
PATH=/rustup/bin:${PATH}  
  
RUN env \  
&& apt-get update \  
&& apt-get -y install --no-install-recommends \  
curl \  
&& curl https://sh.rustup.rs -sSf | \  
sh -s -- --default-toolchain ${RUST_TOOLCHAIN} -y \--no-modify-path \  
&& apt-get -y \--purge remove \  
curl \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove  
  
RUN rustup target add asmjs-unknown-emscripten \  
&& rustup target add wasm32-unknown-emscripten  
  
RUN rustup show \  
&& rustc --version \--verbose \  
&& cargo --version \--verbose  

