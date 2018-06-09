FROM alpine:3.7  
ENV GOPATH=/go  
  
WORKDIR /go/src/app  
ADD . /go/src/app/  
  
RUN apk --no-cache add ca-certificates git go musl-dev \  
&& go get ./... \  
&& go test -v \  
&& CGO_ENABLED=0 go build -ldflags '-s -extldflags "-static"' -o /ssh-key-
manager . \  
&& apk del go git musl-dev \  
&& rm -rf $GOPATH  
  
CMD [ "/ssh-key-manager" ]  

