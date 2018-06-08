FROM golang:1.9 AS builder  
RUN go get github.com/golang/dep/cmd/dep  
  
ENV PROJECT=github.com/ripta/ssp  
ENV CGO_ENABLED=0  
RUN mkdir -p $GOPATH/src/$PROJECT  
COPY . $GOPATH/src/$PROJECT  
RUN cd $GOPATH/src/$PROJECT && dep ensure  
RUN go build -v -ldflags "-s -w -X main.BuildVersion=$VERSION -X
main.BuildDate=$BUILD_DATE -X main.BuildEnvironment=prod" -o /ssp
$PROJECT/cmd/ssp  
  
FROM alpine  
COPY \--from=builder /ssp /app/ssp  
COPY examples/userdir.yaml /app/config.yaml  
ENTRYPOINT ["/app/ssp"]  
CMD ["--config=/app/config.yaml"]  

