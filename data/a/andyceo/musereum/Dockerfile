FROM andyceo/musereum:builder as builder  
MAINTAINER Andrey Andreev <andyceo@yandex.ru> (@andyceo)  
COPY . /build/parity  
RUN cd /build/parity && \  
cargo build --verbose --release --features final && \  
strip /build/parity/target/release/parity  
  
FROM debian:stretch-slim  
MAINTAINER Andrey Andreev <andyceo@yandex.ru> (@andyceo)  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends \  
openssl && \  
apt-get clean && apt-get autoremove && rm -r /var/lib/apt/lists/* && rm -rf
/tmp/* /var/tmp/*  
COPY \--from=builder /build/parity/target/release/parity /musereum  
COPY \--from=builder /build/parity/musereum-testnet-genesis.json /musereum-
testnet-genesis.json  
COPY \--from=builder /build/parity/musereum-node.toml /musereum-node.toml  
WORKDIR /root  
VOLUME ["/root"]  
EXPOSE 30300 8545 8180 8450  
ENTRYPOINT ["/musereum", "--config=/musereum-node.toml", "--force-sealing"]  

