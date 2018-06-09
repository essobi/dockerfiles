FROM ubuntu:xenial  
MAINTAINER yasuyuky <yasuyuki.ymd@gmail.com>  
  
RUN apt-get -y update && apt-get -y install curl gcc pkg-config  
ENV RUST_VERSION 1.25.0  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain
${RUST_VERSION}  
ENV PATH $PATH:/root/.cargo/bin  
RUN mkdir source  
WORKDIR /source  
CMD ["bash"]  

