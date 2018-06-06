FROM frolvlad/alpine-glibc:alpine-3.4  
ENV NOMAD_VERSION=0.4.0 \  
NOMAD_SHA256=c0479dcc03d35c1b0f6e7be256732431384bec16901a124dd97b2a60d465fb91  
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

