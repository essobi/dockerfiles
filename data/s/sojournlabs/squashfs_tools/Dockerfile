# Root certificate authority container.  
FROM debian  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
RUN apt-get update  
RUN apt-get install -y \  
cpio \  
openssl \  
squashfs-tools  
RUN mkdir -p vapr  
WORKDIR /vapr

