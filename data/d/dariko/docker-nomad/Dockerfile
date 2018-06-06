FROM frolvlad/alpine-glibc:alpine-3.4  
ENV NOMAD_VERSION=0.4.1 \  
NOMAD_SHA256=0cdb5dd95c918c6237dddeafe2e9d2049558fea79ed43eacdfcd247d5b093d67  
RUN apk add --update ca-certificates wget && \  
wget -O /nomad_${NOMAD_VERSION}_linux_amd64.zip
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
&& \  
echo "${NOMAD_SHA256} nomad_${NOMAD_VERSION}_linux_amd64.zip" > /nomad.sha256
&& \  
sha256sum -c /nomad.sha256 && \  
cd /usr/local/bin && \  
unzip /nomad_${NOMAD_VERSION}_linux_amd64.zip && \  
apk del ca-certificates wget && \  
rm -rfv /nomad* /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/nomad"]  

