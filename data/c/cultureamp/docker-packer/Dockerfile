FROM buildpack-deps:jessie  
  
MAINTAINER SRE Team <techops@cultureamp.com>  
  
ENV PACKER_VERSION 0.10.1  
ENV PACKER_BINARY packer_${PACKER_VERSION}_linux_amd64.zip  
  
RUN apt-get update \  
&& apt-get install unzip  
  
RUN curl -O -sS -L
https://releases.hashicorp.com/packer/$PACKER_VERSION/$PACKER_BINARY \  
&& unzip ${PACKER_BINARY} -d /usr/local/bin/ \  
&& rm ${PACKER_BINARY}  
  
WORKDIR /usr/src/myapp  

