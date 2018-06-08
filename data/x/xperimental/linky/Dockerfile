FROM golang:1.10.0 AS builder  
  
RUN apt-get update && apt-get install -y upx  
  
ENV PACKAGE=github.com/xperimental/linky  
  
RUN mkdir -p /go/src/${PACKAGE}  
WORKDIR /go/src/${PACKAGE}  
  
ENV LD_FLAGS="-w"  
ENV CGO_ENABLED=0  
COPY . /go/src/${PACKAGE}  
RUN go install -a -v -tags netgo -ldflags "${LD_FLAGS}" .  
RUN upx -9 /go/bin/linky  
  
FROM busybox  
LABEL maintainer="Robert Jacob <xperimental@solidproject.de>"  
  
COPY \--from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=builder /go/bin/linky /bin/linky  
USER nobody  
ENTRYPOINT ["/bin/linky"]  

