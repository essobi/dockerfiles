FROM rust:1.23.0  
RUN apt-get update; \  
apt-get install -y --no-install-recommends \  
git build-essential autoconf automake libtool unzip  
  
WORKDIR /usr/src  
RUN git clone https://github.com/google/protobuf -b v3.5.1 --depth 1  
  
WORKDIR /usr/src/protobuf  
  
RUN ./autogen.sh && \  
./configure --prefix=/usr && \  
make -j 3 && \  
make check && \  
make install  
  
WORKDIR /usr/src  
RUN rm -rf ./protobuf  
  
WORKDIR /usr/src/cloudstore  
COPY . .  
  
RUN cargo install  
  
CMD ["server"]

