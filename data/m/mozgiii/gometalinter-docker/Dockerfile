FROM golang:alpine as builder  
  
RUN apk add --no-cache git  
  
RUN go get -u gopkg.in/alecthomas/gometalinter.v2 \  
&& gometalinter.v2 --install --vendored-linters \  
&& mv /go/bin/* /usr/local/bin/ \  
&& rm -rf /go/pkg /go/*/* \  
&& mv /usr/local/bin/gometalinter.v2 /usr/local/bin/gometalinter  
  
CMD [ "gometalinter", "--vendor", "./..." ]  

