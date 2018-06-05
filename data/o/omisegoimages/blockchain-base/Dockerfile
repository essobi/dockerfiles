FROM omisegoimages/jenkins-slave-elixir:1.6-otp20  
MAINTAINER Kridsada Thanabulpong <sirn@omise.co>  
  
ENV GETHPATH="/go-ethereum"  
ENV PATH="/usr/local/go/bin:${PATH}"  
ENV GOLANG_VERSION="1.9.2"  
RUN set -xe && \  
GOLANG_DOWNLOAD_URL="https://golang.org/dl/go${GOLANG_VERSION}.linux-
amd64.tar.gz" && \  
GOLANG_DOWNLOAD_SHA256="de874549d9a8d8d8062be05808509c09a88a248e77ec14eb77453530829ac02b"
&& \  
curl -fSL -o golang-bin.tar.gz "${GOLANG_DOWNLOAD_URL}" && \  
echo "${GOLANG_DOWNLOAD_SHA256} golang-bin.tar.gz" | sha256sum -c - && \  
tar -xzC /usr/local -f golang-bin.tar.gz && \  
rm golang-bin.tar.gz && \  
go version  
  
# NOTE: fixed version 1.8.6 for now  
ENV GETH_VERSION="v1.8.6"  
# geth  
# NOTE: getting from ppa doesn't work, so building from source  
RUN set -xe && \  
mkdir -p ${GETHPATH} && \  
cd ${GETHPATH} && \  
git init && \  
git remote add origin https://github.com/ethereum/go-ethereum && \  
git fetch --depth 1 origin "${GETH_VERSION}" && \  
git checkout FETCH_HEAD && \  
make geth && \  
install "${GETHPATH}/build/bin/geth" /usr/local/bin && \  
geth version  
  
# populus-required stuff  
RUN set -xe && \  
apt-get install -y python3 python3-dev python3-pip libssl-dev && \  
update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \  
update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 && \  
pip install populus  
  
# libsecp256k1 required stuff  
RUN set -xe && \  
apt-get install -y libgmp3-dev  
  
USER jenkins  

