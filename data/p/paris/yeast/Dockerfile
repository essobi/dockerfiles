FROM ubuntu:16.04 as builder  
  
ARG UNISON_VERSION=2.51.0  
RUN apt-get -qq update && \  
apt-get -qq install build-essential software-properties-common opam && \  
eval $(opam config env)  
  
RUN wget https://github.com/bcpierce00/unison/archive/v$UNISON_VERSION.tar.gz
&& \  
tar -xzvf v$UNISON_VERSION.tar.gz && \  
cd unison-$UNISON_VERSION && \  
make  
  
RUN mkdir -p /usr/src/unison && \  
cd unison-$UNISON_VERSION/src && \  
cp -t /usr/src/unison unison unison-fsmonitor  
  
FROM ubuntu:16.04  
VOLUME ["/mnt/data"]  
WORKDIR /mnt/data  
  
COPY \--from=builder /usr/src/unison/* /usr/local/bin/  
COPY src/* /usr/local/bin/  

