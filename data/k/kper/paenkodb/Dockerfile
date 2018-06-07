FROM ubuntu:14.04  
RUN mkdir /code  
  
VOLUME /config.toml  
VOLUME /data  
  
WORKDIR /code  
  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y git openssl
curl automake gcc g++ libtool make pkg-config libssl-dev  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --disable-sudo
-y --channel=nightly  
  
RUN libtoolize && git clone https://github.com/sandstorm-io/capnproto.git &&
cd capnproto/c++ && ./setup-autotools.sh \  
&& autoreconf -i && ./configure && make -j6 check && make install  
  
RUN git clone https://github.com/paenko/paenkodb  
WORKDIR /code/paenkodb/src  
RUN cargo build --release  
  
EXPOSE 9000  
EXPOSE 3000  
CMD ["/code/paenkodb/target/release/paenkodb","server","/config/config.toml"]  

