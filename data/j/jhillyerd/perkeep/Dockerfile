# Multi-stage docker build for perkeep  
ARG GOLANG_VERSION=1.8  
FROM golang:${GOLANG_VERSION}-alpine as builder  
ARG PERKEEP_REF=8f1a7df176  
  
# Dependencies  
RUN apk add --no-cache git ca-certificates sqlite-dev  
RUN mkdir -p /go/src  
  
# Build perkeep  
RUN git clone https://camlistore.googlesource.com/camlistore
/go/src/perkeep.org  
WORKDIR /go/src/perkeep.org  
RUN git checkout "$PERKEEP_REF"  
RUN go run make.go  
  
# Build genkey  
WORKDIR /go/src/github.com/jhillyerd/perkeep-docker  
COPY . .  
RUN go install ./...  
  
# Package minimal image  
FROM alpine:3.5  
RUN apk add --no-cache ca-certificates libjpeg-turbo-utils  
WORKDIR /usr/bin  
COPY \--from=builder /go/src/perkeep.org/bin/camlistored .  
COPY \--from=builder /go/bin/genkey .  
COPY run-perkeep.sh /  
RUN adduser -g Perkeep -D perkeep  
RUN mkdir /config && chown perkeep: /config  
RUN mkdir /storage && chown perkeep: /storage  
  
# Run perkeep  
VOLUME /config  
VOLUME /storage  
EXPOSE 3179  
USER perkeep  
CMD ["/run-perkeep.sh"]  

