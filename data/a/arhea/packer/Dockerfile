FROM alpine:latest  
  
ENV PACKER_VERSION=1.0.3  
ENV
PACKER_SHA256SUM=0e10169ef9cf3fd55dcc9dc213b9995170f7712e8a162ca2f5109d62bfbe7529  
  
RUN apk add --update git curl openssh bash openssl wget \  
&& curl
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
> packer_${PACKER_VERSION}_linux_amd64.zip \  
&& echo "${PACKER_SHA256SUM} packer_${PACKER_VERSION}_linux_amd64.zip" >
packer_${PACKER_VERSION}_SHA256SUMS \  
&& sha256sum -cs packer_${PACKER_VERSION}_SHA256SUMS \  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin \  
&& rm -f packer_${PACKER_VERSION}_linux_amd64.zip  
  
ENTRYPOINT ["/bin/packer"]  

