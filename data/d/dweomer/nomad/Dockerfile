FROM dweomer/hashibase as verify  
  
WORKDIR /tmp  
  
ARG NOMAD_VERSION=0.8.1  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_SHA256SUMS
.  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_SHA256SUMS.sig
.  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
.  
  
RUN gpg --verify nomad_${NOMAD_VERSION}_SHA256SUMS.sig
nomad_${NOMAD_VERSION}_SHA256SUMS  
RUN grep linux_amd64.zip nomad_${NOMAD_VERSION}_SHA256SUMS | sha256sum -cs  
RUN unzip nomad_${NOMAD_VERSION}_linux_amd64.zip -d /usr/local/bin  
  
FROM frolvlad/alpine-glibc  
  
COPY \--from=verify /usr/local/bin/* /usr/local/bin/  
  
RUN nomad version  
  
ENTRYPOINT ["nomad"]  
CMD ["help"]  

