# Base image to be used.  
FROM alpine:3.7  
# Maintainer of the Dockerfile.  
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"  
  
# Metadata information.  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/breakingpitt/docker-vault"  
  
# Set environment variables for non interactive.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set environment variable for downloading vault version.  
ENV VAULT_VERSION=0.9.3  
# Update the apk indexes and installs HashiCorp Vault.  
# Following the best practices for Dockerfiles we do all the apk stuff  
# in a single line execution.  
RUN apk update \  
&& apk add --update \  
ca-certificates \  
unzip \  
wget \  
&& rm -rf /var/cache/apk/* \  
&& wget -P /tmp/
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
\  
&& mkdir -p /opt/vault \  
&& unzip /tmp/vault_${VAULT_VERSION}_linux_amd64.zip -d /opt/vault  
  
# Volume to store Terraform data.  
VOLUME ["/data"]  
  
# Set workdir directory.  
WORKDIR /data  
  
# Entrypoint command for the container.  
ENTRYPOINT ["/opt/packer/vault"]  
  
# Default command for the container.  
CMD ["--help"]  

