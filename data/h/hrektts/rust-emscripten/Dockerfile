FROM hrektts/emscripten:1.37.22  
LABEL maintainer="mps299792458@gmail.com" \  
version="1.37.22"  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser --uid 1000 --disabled-login --gecos 'Developper' dev \  
&& passwd -d dev \  
&& gpasswd -a dev sudo \  
&& chown -R dev:dev /emsdk_portable  
  
USER dev  
ENV PATH=/home/dev/.cargo/bin:$PATH  
RUN wget -qO - https://sh.rustup.rs | sh -s -- -y --default-toolchain nightly
\  
&& rustup target add asmjs-unknown-emscripten \  
&& rustup target add wasm32-unknown-emscripten  
  
WORKDIR /data  
VOLUME ["/data"]  

