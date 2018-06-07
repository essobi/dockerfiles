# -*- mode: dockerfile -*-  
#  
# An example Dockerfile showing how to build a Rust executable using this  
# image, and deploy it with a tiny Alpine Linux container.  
# Our first FROM statement declares the build environment.  
FROM ekidd/rust-musl-builder:1.25.0 AS builder  
  
# Add our source code.  
COPY . ./  
  
# Fix permissions on source code.  
RUN sudo chown -R rust:rust ./  
  
RUN rustup toolchain remove nightly  
  
RUN rustup default nightly  
  
RUN rustup target add x86_64-unknown-linux-musl  
  
# Build our application.  
RUN cargo build --release  
  
# Now, we need to build our _real_ Docker container, copying in `using-
diesel`.  
FROM alpine:3.7  
RUN apk --no-cache add ca-certificates  
  
ENV ROCKET_ADDRESS=0.0.0.0  
ENV ROCKET_PORT=80  
ENV DATABASE_URL=/data/db.sqlite  
  
RUN mkdir -p /data  
  
EXPOSE 80  
  
COPY \--from=builder \  
/home/rust/src/target/x86_64-unknown-linux-musl/release/service-api \  
/bin/  
CMD /bin/service-api

