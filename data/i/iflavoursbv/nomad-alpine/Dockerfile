#  
# Nomad running on Alpine Linux image with glibc  
#  
  
FROM frolvlad/alpine-glibc  
MAINTAINER IFlavours's Docker Team <docker@iflavours.nl>  
  
ENV NOMAD_VERSION 0.5.6  
ENV NOMAD_RELEASE
https://releases.hashicorp.com/nomad/$NOMAD_VERSION/nomad_${NOMAD_VERSION}_linux_amd64.zip  
  
# ca-certificates is needed to verify releases.hashicorp.com's certificate  
RUN apk add \--update bash wget tar ca-certificates \  
&& wget ${NOMAD_RELEASE} -O nomad.zip -o /dev/null \  
&& cd /usr/local/bin \  
&& unzip /nomad.zip \  
&& nomad \--version \  
&& apk del wget tar ca-certificates \  
&& rm -rf /nomad* /var/cache/apk/*  
  
VOLUME [ "/scripts" ]  
WORKDIR /scripts  
ENTRYPOINT ["/usr/local/bin/nomad"]  

