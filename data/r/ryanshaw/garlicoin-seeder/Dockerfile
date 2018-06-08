FROM ubuntu:xenial-20180112.1 AS build_step  
  
RUN set -ex ; \  
apt update ; \  
apt install build-essential libboost-all-dev libssl-dev -yq ; \  
mkdir -p /src  
  
ADD src /src  
  
WORKDIR /src  
  
RUN set -ex ; \  
make  
  
FROM ubuntu:xenial-20180112.1  
COPY \--from=build_step /src/dnsseed /usr/bin/dnsseed  
COPY \--from=build_step /lib/x86_64-linux-gnu/libcrypto.so.1.0.0
/lib/x86_64-linux-gnu/libcrypto.so.1.0.0  
  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/usr/bin/dnsseed"]  

