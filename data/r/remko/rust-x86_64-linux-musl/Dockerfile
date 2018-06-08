FROM debian:jessie  
MAINTAINER Remko Tronçon <remko@el-tramo.be>  
  
RUN apt-get update && \  
apt-get install -y gcc file curl && \  
(curl https://sh.rustup.rs -sSf | sh -s -- -y) && \  
(. /root/.cargo/env && rustup target add x86_64-unknown-linux-musl) && \  
echo 'source $HOME/.cargo/env' >> $HOME/.bashrc  
  
WORKDIR /src  
VOLUME /root/.cargo/registry  
CMD ["/root/.cargo/bin/cargo", "build", "--target", "x86_64-unknown-linux-
musl", "--release"]  

