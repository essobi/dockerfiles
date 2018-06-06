FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y curl xz-utils libdb-dev libleveldb-dev libsodium-dev
zlib1g-dev libtinfo-dev netbase  
  
RUN mkdir /var/data  
WORKDIR /var/data  
  
ENV VERSION=0.3.2  
RUN curl -L
https://github.com/jpmorganchase/constellation/releases/download/v${VERSION}/constellation-${VERSION}-ubuntu1604.tar.xz
| tar -xJC /usr/local/bin --strip-components=1 -f -  
  
ENTRYPOINT ["constellation-node"]  

