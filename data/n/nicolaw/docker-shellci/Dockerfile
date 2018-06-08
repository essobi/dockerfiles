FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
bashdb \  
bash-static \  
bc \  
shellcheck \  
jq \  
go-md2man \  
bc \  
xml2 \  
curl \  
util-linux \  
coreutils \  
grep \  
rpm \  
devscripts \  
quilt \  
git \  
gnupg \  
sed \  
rsync \  
wget \  
openssl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PACKER_VERSION=1.0.1  
ENV
PACKER_SHA256SUM=b6e126a63a4a2bbe82f9d6bdd48ae879c4f4ffa256b2e1f9567887c321929641  
  
ADD
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
./  
ADD
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS
./  
  
RUN sed -i "/packer_${PACKER_VERSION}_linux_amd64.zip/!d"
packer_${PACKER_VERSION}_SHA256SUMS  
RUN sha256sum -c packer_${PACKER_VERSION}_SHA256SUMS  
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin  
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip  
  

