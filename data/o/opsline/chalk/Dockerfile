FROM golang:latest AS chalk  
  
COPY . /go/src/github.com/opsline/chalk  
WORKDIR /go/src/github.com/opsline/chalk  
RUN make install \  
&& cp /go/bin/chalk /usr/local/bin/  
  
FROM debian:stretch  
COPY \--from=chalk /go/bin/chalk /usr/local/bin/chalk  

