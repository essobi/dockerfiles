FROM golang:1.5  
MAINTAINER Hugo González Labrador  
  
ENV CLAWIO_LOCALSTOREDATA_DATADIR /tmp  
ENV CLAWIO_LOCALSTOREDATA_TMPDIR /tmp  
ENV CLAWIO_LOCALSTOREDATA_PORT 57002  
ENV CLAWIO_LOCALSTOREDATA_CHECKSUM md5  
ENV CLAWIO_LOCALSTOREDATA_PROP "service-localstore-prop:57003"  
ENV CLAWIO_SHAREDSECRET secret  
  
ADD . /go/src/github.com/clawio/service.localstore.data  
WORKDIR /go/src/github.com/clawio/service.localstore.data  
  
RUN go get -u github.com/tools/godep  
RUN godep restore  
RUN go install  
  
ENTRYPOINT /go/bin/service.localstore.data  
  
EXPOSE 57002  

