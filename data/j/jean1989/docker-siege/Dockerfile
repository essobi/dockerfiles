FROM debian:stable-slim as builder  
  
ARG VERSION="v4.0.4"  
  
ENV TARGET_URL=""  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get --no-install-recommends -yq install \  
curl \  
openssl \  
libcurl4-openssl-dev \  
ca-certificates \  
build-essential \  
tar \  
automake \  
autoconf \  
zlib1g-dev && \  
curl -o siege.tar.gz -sSL
https://github.com/JoeDog/siege/archive/${VERSION}.tar.gz && \  
tar -xf siege.tar.gz && \  
cd siege-${VERSION#"v"} && \  
./utils/bootstrap && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf siege-${VERSION#"v"} && \  
rm -rf siege.tar.gz && \  
apt-get -yq clean && \  
apt-get -yq autoclean && \  
apt-get -yq remove automake autoconf curl zlib1g-dev && \  
apt-get -yq autoremove && \  
rm -rf /var/lib/apt/lists  
  
FROM debian:stable-slim  
  
COPY \--from=builder /usr/local/bin/siege /usr/local/bin  
COPY \--from=builder /usr/local/etc/siegerc /usr/local/etc  

