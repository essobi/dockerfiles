FROM rust:latest  
MAINTAINER Matsievskiy Sergey "MatsievskiySV@gmail.com"  
RUN apt-get update && apt-get install git  
RUN git clone https://seregaxvm@bitbucket.org/seregaxvm/overseer.git
/usr/src/overseer  
WORKDIR /usr/src/overseer  
ENV RUST_LOG INFO  
  
RUN cargo build --release  
EXPOSE 9090  
CMD ["cargo", "run", "--release"]

