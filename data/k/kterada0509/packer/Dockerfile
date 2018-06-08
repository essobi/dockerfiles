FROM alpine:latest  
  
LABEL maintainer="kterada.0509sg@gmail.com"  
  
ENV PACKER_VERSION=1.1.2  
RUN apk --update add git bash bzr git mercurial subversion openssh-client ca-
certificates curl  
RUN curl -LOs
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip  
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/bin/  
RUN rm -rf /var/cache/apk/* packer_${PACKER_VERSION}_linux_amd64.zip  
  
CMD ["/usr/bin/packer"]  

