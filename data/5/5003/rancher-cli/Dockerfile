FROM alpine:edge  
RUN apk add \--no-cache \--virtual .buildpack-deps \  
ca-certificates \  
curl \  
tar && \  
curl \--location
https://github.com/rancher/cli/releases/download/v0.6.4/rancher-linux-
amd64-v0.6.4.tar.gz \  
| tar \--gzip \--extract \--file \- \--directory /usr/local/bin/ \--strip-
components 2 && \  
apk del \--no-cache .buildpack-deps  
WORKDIR /work/  
CMD ["ash"]

