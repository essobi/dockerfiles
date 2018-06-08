FROM golang:1.8-alpine  
  
LABEL maintainer "moogar0880@gmail.com"  
  
RUN apk --update upgrade && \  
apk add make git && \  
rm -rf /var/cache/apk/*  
  
RUN go get -u gopkg.in/alecthomas/gometalinter.v1 && \  
ln /go/bin/gometalinter.v1 /go/bin/gometalinter && \  
gometalinter --install  
  
ENTRYPOINT ["/go/bin/gometalinter"]  
CMD ["--help"]  

