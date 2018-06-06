FROM ubuntu:artful as builder  
MAINTAINER Otaci <otaci@protonmail.com>  
  
ARG USER_ID  
ARG GROUP_ID  
  
ENV HOME /bitcoin  
ENV USER_ID ${USER_ID:-1000}  
ENV GROUP_ID ${GROUP_ID:-1000}  
  
RUN groupadd -g ${GROUP_ID} bitcoin \  
&& useradd -u ${USER_ID} -g bitcoin -s /bin/bash -m -d /bitcoin bitcoin  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git build-essential libtool autotools-dev automake pkg-config \  
libssl-dev bsdmainutils libboost-all-dev libevent-dev \  
libzmq3-dev  
  
RUN cd /bitcoin && mkdir bin && git config --global http.sslVerify "false" &&
\  
git clone https://github.com/BitcoinUnlimited/BitcoinUnlimited.git && \  
cd BitcoinUnlimited && git checkout -b bucash1.1.1.1 bucash1.1.1.1  
  
RUN cd /bitcoin/BitcoinUnlimited && ./autogen.sh && \  
./configure --disable-wallet --disable-tests --prefix=/bitcoin && \  
make install && cd /bitcoin && rm -rf BitcoinUnlimited  
  
FROM alpine:latest  
  
RUN mkdir -p /bitcoin/bin  
  
COPY \--from=builder /bitcoin/bin/* /bitcoin/bin/  

