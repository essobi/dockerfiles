FROM ubuntu:16.04  
MAINTAINER info@funkwerk-itk.com  
  
# FIXME: Tini is deprecated:  
# NOTE: If you are using Docker 1.13 or greater, Tini is included in Docker
itself.  
# This includes all versions of Docker CE. To enable Tini, just pass the
--init flag to docker run.  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Preinstall xmllint  
RUN apt-get -y update && apt-get -y install libxml2-utils && \  
rm -rf /var/lib/apt/lists/*  

