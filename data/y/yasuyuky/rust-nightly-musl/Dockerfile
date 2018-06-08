FROM rustlang/rust:nightly  
  
RUN apt-get -y update && apt-get -y install musl-tools  
  
RUN rustup target add x86_64-unknown-linux-musl  

