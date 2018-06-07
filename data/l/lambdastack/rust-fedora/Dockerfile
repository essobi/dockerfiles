FROM fedora:latest  
MAINTAINER Chris Jones "chris.jones@lambdastack.io"  
RUN dnf -y update && dnf clean all  
RUN dnf -y install git gcc curl openssl openssl-devel ca-certificates tar &&
dnf clean all  
  
ENV RUST_ARCHIVE=rust-1.14.0-x86_64-unknown-linux-gnu.tar.gz  
ENV RUST_DOWNLOAD_URL=https://static.rust-lang.org/dist/$RUST_ARCHIVE  
  
RUN mkdir /rust  
WORKDIR /rust  
  
RUN curl -fsOSL $RUST_DOWNLOAD_URL \  
&& curl -s $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -C /rust -xzf $RUST_ARCHIVE \--strip-components=1 \  
&& rm $RUST_ARCHIVE \  
&& ./install.sh  

