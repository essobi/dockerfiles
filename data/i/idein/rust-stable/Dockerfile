FROM ubuntu:18.04  
MAINTAINER Yasuyuki YAMADA <yasuyuky@idein.jp>  
  
RUN apt-get -y update\  
&& apt-get -y install --no-install-recommends curl ca-certificates gcc libc6
pkg-config git openssh-client\  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
ENV RUST_VERSION 1.26.0  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain
${RUST_VERSION}  
ENV PATH $PATH:/root/.cargo/bin  
RUN rustup component add rustfmt-preview  
RUN mkdir source  
WORKDIR /source  
CMD ["bash"]  

