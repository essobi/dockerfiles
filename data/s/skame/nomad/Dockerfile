FROM frolvlad/alpine-glibc:3.2  
ENV NOMAD_VERSION=0.2.3 \  
NOMAD_SHA256=0f3a7083d160893a291b5f8b4359683c2df7991fa0a3e969f8785ddb40332a8c  
RUN apk add --update ca-certificates wget coreutils && \  
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

