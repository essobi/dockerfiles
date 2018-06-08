FROM golang:alpine  
  
WORKDIR /go/src/github.com/PolarGeospatialCenter/pgcboot  
ENV BINARY distroserver  
  
RUN apk add --no-cache git make curl  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
COPY Gopkg.toml Gopkg.lock Makefile ./  
RUN make deps  
  
COPY cmd ./cmd  
COPY pkg ./pkg  
RUN go build -o /bin/$BINARY ./cmd/$BINARY  
  
FROM alpine:latest  
ENV SSH_KNOWN_HOSTS=/root/known_hosts  
  
RUN apk add --no-cache ca-certificates  
ADD https://github.com/coreos/container-linux-config-
transpiler/releases/download/v0.5.0/ct-v0.5.0-x86_64-unknown-linux-gnu
/usr/bin/ct  
COPY assets/known_hosts $SSH_KNOWN_HOSTS  
RUN chmod a+x /usr/bin/ct  
  
COPY \--from=0 /bin/$BINARY /bin/$BINARY  
CMD ["/bin/distroserver"]  

