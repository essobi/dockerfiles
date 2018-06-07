FROM golang:1.5  
MAINTAINER Hugo González Labrador  
  
ENV CLAWIO_LOCALSTOREPROP_PORT 57003  
ENV CLAWIO_LOCALSTOREPROP_DSN "root:admin@tcp(service-localstore-prop-
mysql:3306)/prop"  
ENV CLAWIO_SHAREDSECRET secret  
  
ADD . /go/src/github.com/clawio/service.localstore.prop  
WORKDIR /go/src/github.com/clawio/service.localstore.prop  
  
RUN go get -u github.com/tools/godep  
RUN godep restore  
RUN go install  
  
ENTRYPOINT /go/bin/service.localstore.prop  
  
EXPOSE 57003  

