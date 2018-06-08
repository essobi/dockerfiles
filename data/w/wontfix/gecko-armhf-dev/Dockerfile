FROM ubuntu:16.04  
MAINTAINER Makoto Kato <m_kato@ga2.so-net.ne.jp>  
  
ADD sources.list /etc/apt/  
RUN mkdir /mozilla  
RUN mkdir /root/.mozbuild  
ADD mozconfig.sample /mozilla/  
RUN dpkg --add-architecture armhf  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
autoconf2.13 \  
build-essential \  
ccache \  
clang-3.9 \  
curl \  
g++ \  
g++-4.9-arm-linux-gnueabihf \  
g++-arm-linux-gnueabihf \  
llvm-3.9 \  
mercurial \  
python \  
unzip \  
zip && \  
apt-get install -y --no-install-recommends \  
libasound2-dev:armhf \  
libdbus-glib-1-dev:armhf \  
libgconf2-dev:armhf \  
libpulse-dev:armhf \  
libxt-dev:armhf \  
libgtk2.0-dev:armhf \  
libgtk-3-dev:armhf \  
mesa-common-dev:armhf && \  
apt-get clean  
  
RUN curl https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-
gnu/rustup-init -o rustup-init && \  
chmod +x rustup-init && \  
./rustup-init -y && \  
rm rustup-init  
ENV PATH=$PATH:/root/.cargo/bin  
RUN /root/.cargo/bin/rustup target add armv7-unknown-linux-gnueabihf  
  
ENV SHELL=/bin/bash  
ENV NO_MERCURIAL_SETUP_CHECK=1  

