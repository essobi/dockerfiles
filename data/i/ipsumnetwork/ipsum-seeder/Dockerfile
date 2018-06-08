FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get --no-install-recommends --yes install \  
build-essential \  
libboost-all-dev \  
libssl-dev  
  
WORKDIR /ips  
  
COPY . .  
  
RUN make  
  
ENTRYPOINT ["/ips/dnsseed"]  

