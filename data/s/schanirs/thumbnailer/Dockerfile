FROM rust:1.23.0  
WORKDIR /usr/src/myapp  
COPY . .  
RUN cargo build --release  
  
FROM debian:latest  
COPY \--from=0 /usr/src/myapp/target/release/schani_thumbnailer /usr/local/bin  
EXPOSE 8000  
ENTRYPOINT ["/usr/local/bin/schani_thumbnailer"]  

