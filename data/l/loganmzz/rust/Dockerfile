FROM buildpack-deps:stretch-scm  
  
LABEL maintainer="Logan Mzz"  
  
LABEL org.rust-lang.version="1.26.1"  
LABEL org.rust-lang.channel="stable"  
LABEL org.rust-lang.release-date="2018-05-29"  
  
ENV RUST_VERSION 1.26.1  
RUN apt update \  
&& apt install -y dpkg-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -r rust && useradd -r -g rust -m rust  
  
USER rust  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain
${RUST_VERSION}  
  
ENV PATH /home/rust/.cargo/bin:$PATH  
  
ENV HOME /home/rust  

