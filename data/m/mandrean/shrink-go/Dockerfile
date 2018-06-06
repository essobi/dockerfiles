FROM golang:1.9-alpine3.6  
LABEL maintainer="Sebastian Mandrean <sebastian.mandrean@gmail.com>"  
  
# Environment variables  
ENV GOOS linux  
ENV GOARCH amd64  
ENV CGO_ENABLED 0  
ENV ALPINE_MIRROR http://dl-3.alpinelinux.org/alpine  
  
# Install dependencies  
RUN printf "@community ${ALPINE_MIRROR}/edge/community/" >>
"/etc/apk/repositories" && \  
apk --no-cache add \  
git \  
curl \  
upx@community && \  
apk --no-cache del wget  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /go/src  

