FROM rust:1.26.2  
WORKDIR /usr/src/myapp  
COPY . .  
RUN cargo build --release  
  
FROM schanirs/rawtherapee  
COPY \--from=0 /usr/src/myapp/target/release/schani_processor /usr/local/bin  
  
ENTRYPOINT ["schani_processor"]  

