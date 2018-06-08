FROM alpine:3.6  
MAINTAINER Nordstrom Kubernetes Platform Team "techk8s@nordstrom.com"  
RUN apk --update upgrade \  
&& apk --update --no-cache add \  
ca-certificates \  
curl \  
shadow \  
&& rm -rf /var/cache/apk/*  
  
COPY nordstrom-ca-certs/ /etc/ssl/nordstrom-ca-certificates/  
  
RUN useradd --create-home --shell /bin/bash nordstrom  
USER nordstrom  
WORKDIR /  

