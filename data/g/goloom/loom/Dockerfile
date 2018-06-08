FROM golang:1.10.1  
RUN go get github.com/ahmetb/govvv  
  
COPY . /go/src/github.com/go-loom/loom  
WORKDIR /go/src/github.com/go-loom/loom  
RUN govvv install -pkg github.com/go-loom/loom/pkg/version github.com/go-
loom/loom/cmd/loom/...  
  
ENTRYPOINT ["loom"]  
CMD ["-h"]  

