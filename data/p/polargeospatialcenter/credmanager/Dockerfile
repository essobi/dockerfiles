FROM golang:alpine  
  
WORKDIR /go/src/github.com/PolarGeospatialCenter/credmanager  
  
RUN apk add --no-cache git make curl  
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
COPY Gopkg.toml Gopkg.lock Makefile ./  
RUN make deps  
  
COPY cmd ./cmd  
COPY pkg ./pkg  
RUN go build -o /bin/credmanager ./cmd/credmanager  
  
FROM alpine:latest  
RUN apk add --no-cache ca-certificates  
COPY \--from=0 /bin/credmanager /bin/credmanager  
CMD ["/bin/credmanager"]  

