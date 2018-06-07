FROM iron/go:dev  
LABEL maintainer="technology@bcorporation.net"  
  
ENV SRC_DIR=/go/src/github.com/b-lab-org/impact-go  
ADD . $SRC_DIR  
  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 &&
chmod +x /usr/local/bin/dep  
WORKDIR $SRC_DIR  
RUN dep ensure && \  
go build ./...  
  
WORKDIR $SRC_DIR/cmd/serve  
ENTRYPOINT ["go", "run", "serve.go"]  
EXPOSE 8080 4443

