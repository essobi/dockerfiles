FROM debian:8.0  
MAINTAINER andystanton  
ENV LANG C.UTF-8  
ENV RUST_VERSION 1.0.0-beta  
ENV PATH $PATH:/usr/local/bin  
RUN apt-get update && \  
apt-get install -y patch wget gcc && \  
wget https://static.rust-lang.org/dist/rust-${RUST_VERSION}-x86_64-unknown-
linux-gnu.tar.gz && \  
tar -xvf rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz && \  
rm rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz && \  
/rust-${RUST_VERSION}-x86_64-unknown-linux-gnu/install.sh && \  
rm -rf /rust-${RUST_VERSION}-x86_64-unknown-linux-gnu && \  
apt-get remove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-c-family.sh", "rustc"]  

