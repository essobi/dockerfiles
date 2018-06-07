FROM golang  
  
ADD https://curl.haxx.se/ca/cacert.pem /etc/ssl/certs/ca-certificates.crt  
  
RUN go get github.com/Masterminds/glide && \  
go build github.com/Masterminds/glide  
  
ADD . /go/src/github.com/pivotal-cf/email-resource  
WORKDIR /go/src/github.com/pivotal-cf/email-resource  
  
RUN glide install  
RUN go build -o bin/check check/cmd/*.go && \  
go build -o bin/in in/cmd/*.go && \  
go build -o bin/out out/cmd/*.go  
  
RUN ln -s /go/src/github.com/pivotal-cf/email-resource/bin /opt/resource  

