FROM ubuntu:14.04  
ENV VERSION 0.5.0  
RUN set -ex; \  
apt-get update --quiet=2; \  
apt-get install --assume-yes --no-install-recommends \  
curl \  
# openssl \  
make \  
g++ \  
libssl-dev \  
ca-certificates; \  
rm --recursive --force /var/lib/apt/lists/*;  
  
RUN set -ex; \  
curl -L https://github.com/AGWA/git-crypt/archive/$VERSION.tar.gz | tar zxv -C
/tmp  
  
RUN set -ex; \  
cd /tmp/git-crypt-$VERSION; \  
make; \  
make install PREFIX=/usr/local  

