# Base image to be used.  
FROM ubuntu:17.10  
# Maintainer of the Dockerfile.  
LABEL maintainer "Pedro Garcia Rodriguez <pedgarrod@gmail.com>"  
  
# Set environment variables for non interactive.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set environment variable for downloading packer version.  
ENV PACKER_VERSION=0.11.0  
# build-time variables.  
ARG VCS_REF  
  
#Metadata information.  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/breakingpitt/docker-packer"  
  
# Update the apt indexes and install the required software.  
# Following the best practices for Dockerfiles we do all the apt stuff  
# in a single line execution for avoid unwanted layers in our docker image.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget --no-check-certificate -P /tmp/
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
\  
&& mkdir -p /opt/packer \  
&& unzip /tmp/packer_${PACKER_VERSION}_linux_amd64.zip -d /opt/packer  
  
# Volume to store Terraform data.  
VOLUME ["/data"]  
  
# Set workdir directory.  
WORKDIR /data  
  
# Entrypoint command for the container.  
ENTRYPOINT ["/opt/packer/packer"]  
  
# Default command for the container.  
CMD ["--help"]  

