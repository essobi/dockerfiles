FROM docker:git  
  
MAINTAINER Erwin Steffens <esteffens@rovecom.nl>  
  
ENV S2I_VERSION 1.1.5  
RUN wget https://github.com/openshift/source-to-
image/releases/download/v${S2I_VERSION}/source-to-
image-v${S2I_VERSION}-4dd7721-linux-386.tar.gz -O /tmp/s2i.tar.gz && \  
tar -xvf /tmp/s2i.tar.gz -C /tmp && \  
mv /tmp/s2i /usr/local/bin/s2i && \  
rm /tmp/*  
  
CMD ["s2i", "--version"]

