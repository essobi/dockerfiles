FROM scorpil/rust:stable  
MAINTAINER Jeffrey Boehm "jeff@ressourcenkonflikt.de"  
  
WORKDIR /rust/app  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential \  
libprotobuf-dev \  
libprotoc-dev \  
wget \  
pkg-config && \  
rm -rf /var/lib/apt/lists/* && \  
wget -O- https://github.com/Spotifyd/spotifyd-http/archive/master.tar.gz | \  
tar zxvf - --strip-components=1 && \  
cargo install && \  
apt-get remove --purge -yy \  
build-essential \  
libprotobuf-dev \  
libprotoc-dev \  
wget \  
pkg-config && \  
apt-get autoremove -yy --purge && \  
mv /root/.cargo/bin/spotifyd-http /usr/local/bin/ && \  
rm -rf \  
/root/.cargo/ \  
/rust  
  
EXPOSE 6767  
  
CMD ["--help"]  
ENTRYPOINT ["/usr/local/bin/spotifyd-http"]  

