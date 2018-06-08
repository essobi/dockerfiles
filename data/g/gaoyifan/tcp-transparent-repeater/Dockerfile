FROM rust as builder  
  
ARG TARGET=x86_64-unknown-linux-musl  
  
RUN apt-get update  
RUN apt-get install -y \  
musl-tools \  
xutils-dev  
RUN rustup target add $TARGET  
WORKDIR /usr/src/ttr  
ADD Cargo.toml Cargo.lock /usr/src/ttr/  
ADD src /usr/src/ttr/src/  
RUN cargo build --release --target $TARGET  
RUN strip target/$TARGET/release/tcp_transparent_repeater  
  
FROM scratch  
COPY \--from=builder /usr/src/ttr/target/x86_64-unknown-linux-
musl/release/tcp_transparent_repeater /  
ENTRYPOINT ["/tcp_transparent_repeater"]  

