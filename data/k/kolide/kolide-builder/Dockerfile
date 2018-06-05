FROM golang:1.6.3-alpine  
MAINTAINER Victor Vrantchan <victor@kolide.co> (@groob)  
  
RUN apk add --update git  
  
RUN \  
go get -u -v github.com/Masterminds/glide && \  
go get -u -v gopkg.in/alecthomas/gometalinter.v1  
  
RUN apk add --update \  
nodejs \  
bash \  
alpine-sdk \  
musl-dev \  
openssl  
  
COPY rootfs /  
  
VOLUME /go/src/github.com/kolide/kolide-ose  
WORKDIR /go/src/github.com/kolide/kolide-ose  
  
EXPOSE 8080  
ENTRYPOINT ["/builder.sh"]  
  

