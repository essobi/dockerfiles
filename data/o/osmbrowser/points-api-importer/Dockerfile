FROM rust:1.21  
WORKDIR /usr/src/points-api-importer  
COPY . .  
RUN cargo install  
  
FROM debian:stretch-slim  
COPY \--from=0 /usr/local/cargo/bin/points-api-importer /usr/local/bin/points-
api-importer  
CMD ["points-api-importer"]  

