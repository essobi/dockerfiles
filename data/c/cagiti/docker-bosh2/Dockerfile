FROM alpine:3.5  
MAINTAINER Cai Cooper "caicooper82@gmail.com"  
ARG BOSH_VERSION="2.0.16"  
RUN apk add --no-cache --update unzip curl openssl ca-certificates
libc6-compat \  
&& ln -s /lib/ /lib64  
  
RUN wget -nv https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-${BOSH_VERSION}-linux-amd64 -O /usr/local/bin/bosh2 && \  
chmod 755 /usr/local/bin/bosh2  
  
ENTRYPOINT ["bosh2"]  

