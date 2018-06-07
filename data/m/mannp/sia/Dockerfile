FROM golang as sia  
  
ENV GOOS linux  
ENV GOARCH amd64  
ENV CGO_ENABLED 0  
RUN go get -d -u github.com/NebulousLabs/Sia/... && \  
cd $GOPATH/src/github.com/NebulousLabs/Sia && \  
make release  
  
FROM alpine:latest  
  
RUN apk --no-cache add socat  
  
WORKDIR "/sia"  
COPY \--from=sia /go/bin/siad ./  
COPY \--from=sia go/bin/siac ./  
ENTRYPOINT socat tcp-listen:9980,reuseaddr,fork tcp:localhost:8000 & ./siad
--modules=cgtrw --sia-directory=/mnt/sia --api-addr "localhost:8000"  

