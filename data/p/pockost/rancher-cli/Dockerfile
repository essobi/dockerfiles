FROM alpine:latest  
  
ENV RANCHER_VERSION 0.6.4  
  
RUN apk update && \  
apk add \--no-cache \--virtual .buildpack-deps \  
ca-certificates \  
curl \  
tar && \  
apk add docker && \  
curl \--location
https://github.com/rancher/cli/releases/download/v${RANCHER_VERSION}/rancher-
linux-amd64-v${RANCHER_VERSION}.tar.gz \  
| tar \--gzip \--extract \--file \- \--directory /usr/local/bin/ \--strip-
components 2 && \  
apk del \--no-cache .buildpack-deps  
WORKDIR /work/  
ENTRYPOINT ["rancher"]  

