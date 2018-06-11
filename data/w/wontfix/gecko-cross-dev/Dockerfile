FROM ubuntu:18.04  
MAINTAINER Makoto Kato <m_kato@ga2.so-net.ne.jp>  
  
ADD sources.list /etc/apt/  
RUN mkdir /mozilla /root/.mozbuild  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
autoconf2.13 \  
build-essential \  
ccache \  
clang \  
curl \  
g++ \  
gcc-multilib \  
llvm \  
mercurial \  
python \  
unzip \  
zip && \  
apt-get clean  
RUN curl https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-
gnu/rustup-init -o rustup-init && \  
chmod +x rustup-init && \  
./rustup-init -y && \  
rm rustup-init  
ENV PATH=$PATH:/root/.cargo/bin  
  
#RUN adduser --ingroup users --disabled-password --gecos '' builder  
ENV SHELL=/bin/bash  
ENV NO_MERCURIAL_SETUP_CHECK=1  

