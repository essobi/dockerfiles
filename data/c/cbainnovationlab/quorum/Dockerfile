FROM ubuntu:xenial  
MAINTAINER Dan Turner <dan.turner@cba.com.au>  
  
# Misc Environment Variables  
ENV PATH $PATH:/usr/local/go/bin  
  
# Install Pre Requisites  
RUN apt-get update && \  
apt-get install -y wget software-properties-common unzip git build-essential
runit && \  
add-apt-repository -y ppa:ethereum/ethereum && \  
  
# Install Constellation  
VERSION=0.2.0 && \  
ARCHIVE=constellation-${VERSION}-ubuntu1604.tar.xz && \  
wget -q
https://github.com/jpmorganchase/constellation/releases/download/v${VERSION}/${ARCHIVE}
&& \  
tar --xz -xvf ${ARCHIVE} -C /usr/local/bin --strip-components=1 && \  
rm -rf ${ARCHIVE} && \  
  
# Install Go  
GO_RELEASE=go1.7.3.linux-amd64.tar.gz && \  
wget -q https://storage.googleapis.com/golang/${GO_RELEASE} && \  
tar -xvzf ${GO_RELEASE} && \  
mv go /usr/local/go && \  
rm -rf ${GO_RELEASE} && \  
  
# Clone Quorum and build binaries  
VERSION=v2.0.0 && \  
git clone --branch $VERSION --depth 1
https://github.com/jpmorganchase/quorum.git && \  
cd quorum && \  
make all && \  
# => Copy geth & bootnode binaries & Delete repo  
cp /quorum/build/bin/geth /usr/local/bin && \  
cp /quorum/build/bin/bootnode /usr/local/bin && \  
cd / && rm -rf /quorum && \  
  
# Install runsvinit wrapper  
wget -q
https://github.com/peterbourgon/runsvinit/releases/download/v2.0.0/runsvinit-
linux-amd64.tgz && \  
tar -zxvf runsvinit-linux-amd64.tgz -C /usr/local/bin && \  
rm -rf runsvinit-linux-amd64.tgz && \  
mkdir -p /etc/service/constellation && \  
mkdir -p /etc/service/quorum && \  
  
# Remove unneeded packages  
apt-get remove --purge -y wget software-properties-common unzip build-
essential git $(apt-mark showauto) && \  
# Install SOLC and other dependencies for constellation  
apt-get update && \  
apt-get install -y libdb-dev libleveldb-dev libsodium-dev zlib1g-dev libtinfo-
dev libgmp-dev solc && \  
# Clean up  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/local/go  
  
ADD scripts/run-constellation /etc/service/constellation/run  
ADD scripts/run-quorum /etc/service/quorum/run  
  
ENTRYPOINT ["/usr/local/bin/runsvinit"]  

