FROM debian:stretch  
  
RUN apt-get update \  
&& apt-get install -y curl \  
libssl1.0-dev libpsl-dev libssh-dev \  
gcc g++ \  
make cmake \  
pkg-config git file \  
&& apt-get clean  
  
RUN curl https://sh.rustup.rs -o rustup.sh && \  
chmod +x rustup.sh && \  
./rustup.sh -y && \  
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> /etc/bash.bashrc  
  

