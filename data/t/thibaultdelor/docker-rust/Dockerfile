FROM thibaultdelor/docker-rust:1.13.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
CMD cargo run --release  
  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN cargo build --release  

