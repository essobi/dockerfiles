FROM golang:1.9-alpine  
  
ENV GLIDE_VERSION 0.13.0  
ENV GLIDE_ARCH linux-amd64  
  
RUN apk add --update --virtual build-dep --no-cache curl && \  
mkdir -p $GOPATH/bin && \  
curl -L
"https://github.com/Masterminds/glide/releases/download/v${GLIDE_VERSION}/glide-v${GLIDE_VERSION}-${GLIDE_ARCH}.tar.gz"
| tar xz && \  
mv $GLIDE_ARCH/glide /usr/bin/glide && \  
rm -rf linux-arm64 && \  
apk del build-dep && \  
rm -rf /var/cache/apk/*  

