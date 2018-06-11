FROM golang:latest  
  
RUN apk add --no-cache git; \  
go version; \  
go get github.com/golang/dep/cmd/dep; \  
cd $GOPATH/src/github.com/golang/dep; \  
go install github.com/golang/dep/...; \  
mv $GOPATH/bin/dep /usr/bin;  
  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
ENTRYPOINT ["dep"]  
CMD ["-h"]  

