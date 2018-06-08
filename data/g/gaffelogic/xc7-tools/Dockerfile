FROM rustlang/rust:nightly AS builder  
WORKDIR /source  
COPY . .  
RUN cargo install --bins --path .  
  
FROM ubuntu  
COPY \--from=builder /usr/local/cargo/bin/* /usr/local/bin/

