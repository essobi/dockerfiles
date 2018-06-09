FROM rust:latest  
  
# Required packages by "tarpaulin"  
RUN apt-get update -q && apt-get install -q -y libcurl4-openssl-dev libelf-dev
libdw-dev curl cmake build-essential pkg-config  
  
# Installing "tarpaulin" itself.  
RUN cargo install cargo-tarpaulin  

