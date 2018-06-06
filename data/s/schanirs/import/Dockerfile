FROM rust:1.26.1  
RUN cargo install diesel_cli  
WORKDIR /usr/src/myapp  
COPY . .  
RUN cargo build --release  
  
FROM debian:latest  
RUN apt-get update && \  
apt-get install -y \  
libpq5 \  
libsqlite3-0 \  
libmariadbclient18 \  
\--no-install-recommends  
COPY \--from=0 /usr/src/myapp/target/release/schani_import /usr/local/bin  
COPY \--from=0 /usr/src/myapp/migrations /migrations  
COPY \--from=0 /usr/local/cargo/bin/diesel /usr/local/bin  
EXPOSE 8000  
ENTRYPOINT ["bash", "-c", "cd /migrations && diesel migration run &&
schani_import"]  

