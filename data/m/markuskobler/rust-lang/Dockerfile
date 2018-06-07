FROM debian:jessie  
  
RUN echo "export SHELL=/bin/bash" >> /root/.bashrc  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y \  
sudo \  
git \  
curl \  
python \  
cmake \  
make \  
pkg-config \  
strace \  
valgrind \  
libc-dbg \  
openssl \  
libssl-dev \  
tcpdump \  
dnsutils \  
libcurl4-openssl-dev \  
libelf-dev \  
libdw-dev \  
cmake \  
gcc \  
g++ && \  
apt-get clean autoclean && apt-get autoremove -y && \  
rm -rf /var/lib/apt /var/lib/cache/* /var/lib/log/*  
  
ENV RUST_VERSION=1.1.0  
RUN \  
curl -sL https://static.rust-lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-
linux-gnu.tar.gz | \  
tar xz -C /tmp && \  
/tmp/rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh && \  
rm -rf /tmp/rust-$RUST_VERSION-x86_64-unknown-linux-gnu && \  
rm -rf /usr/local/share/doc/rust  
  
RUN \  
cd /root && curl -sL
https://github.com/SimonKagstrom/kcov/archive/master.tar.gz | tar xz && \  
mkdir kcov-master/build && cd /root/kcov-master/build && cmake .. && make &&
make install && \  
cd /root && rm -rf /root/kcov-master  
  
VOLUME ["/rust"]  
  
WORKDIR /rust  
ENTRYPOINT ["/bin/bash"]  

