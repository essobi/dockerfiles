FROM williamyeh/ansible:alpine3  
  
LABEL maintainer "tomelliff@gmail.com"  
  
ENV PACKER_VERSION=1.2.0  
ENV
PACKER_SHA256SUM=d1b0fcc4e66dfe4919c25752d028a4e4466921bf0e3f75be3bbf1c85082e8040  
  
RUN apk add --update git curl openssh make && \  
curl --silent
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
> packer_${PACKER_VERSION}_linux_amd64.zip && \  
echo "${PACKER_SHA256SUM} packer_${PACKER_VERSION}_linux_amd64.zip" >
packer_${PACKER_VERSION}_SHA256SUMS && \  
cat packer_${PACKER_VERSION}_SHA256SUMS && \  
sha256sum packer_${PACKER_VERSION}_linux_amd64.zip && \  
sha256sum -c packer_${PACKER_VERSION}_SHA256SUMS && \  
unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin && \  
rm -f packer_${PACKER_VERSION}_linux_amd64.zip && \  
adduser -D -u 1000 packer  
  
USER packer  
ENV USER=packer  

