FROM ubuntu:17.10  
ENV RUST_TARGET x86_64-unknown-linux-gnu  
ENV RUST_DISTRIB rust-nightly-$RUST_TARGET  
ENV DOCKER_VERSION 17.05.0-ce  
  
WORKDIR /rust  
ADD rustup-init.sh .  
  
RUN apt-get -y update && apt-get install -q -y \  
build-essential \  
curl \  
git-core \  
openssh-client \  
&& \  
bash rustup-init.sh -y --verbose --default-toolchain=nightly && \  
rm -r /rust && \  
curl -L -o "/tmp/docker-${DOCKER_VERSION}.tgz"
"https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" && \  
tar -xz -C /tmp -f "/tmp/docker-${DOCKER_VERSION}.tgz" && \  
mv /tmp/docker/* /usr/bin  
  
ENV PATH "$PATH:/root/.cargo/bin"  
WORKDIR /  

