FROM liuchong/rustup:nightly  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates zlib1g-dev libc6
libgcc1 cmake libssh2-1-dev git  
  
WORKDIR /build  
ADD . /build  
  
RUN cargo build --release --verbose  
  
# # Production build:  
FROM ubuntu  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates libssl1.0.2  
  
WORKDIR /var/lib/grapple  
ENV ROCKET_ENV=prod  
ENV ROCKET_PORT=8000  
COPY \--from=0 /build/target/release/grapple /bin/grapple  
  
CMD /bin/grapple  

