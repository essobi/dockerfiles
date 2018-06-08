FROM dweomer/hashibase as verify  
  
WORKDIR /tmp  
  
ARG SERF_VERSION=0.8.1  
ADD
https://releases.hashicorp.com/serf/${SERF_VERSION}/serf_${SERF_VERSION}_SHA256SUMS
.  
ADD
https://releases.hashicorp.com/serf/${SERF_VERSION}/serf_${SERF_VERSION}_SHA256SUMS.sig
.  
ADD
https://releases.hashicorp.com/serf/${SERF_VERSION}/serf_${SERF_VERSION}_linux_amd64.zip
.  
  
RUN gpg --verify serf_${SERF_VERSION}_SHA256SUMS.sig
serf_${SERF_VERSION}_SHA256SUMS  
RUN grep linux_amd64.zip serf_${SERF_VERSION}_SHA256SUMS | sha256sum -cs  
RUN unzip serf_${SERF_VERSION}_linux_amd64.zip -d /usr/local/bin  
  
FROM alpine  
  
COPY \--from=verify /usr/local/bin/* /usr/local/bin/  
  
RUN serf version  
  
ENTRYPOINT ["serf"]  
CMD ["help"]  

