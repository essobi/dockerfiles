FROM golang:1.9.2-stretch  
  
RUN go get -d github.com/ellaism/go-ellaism/...  
WORKDIR $GOPATH/src/github.com/ellaism/go-ellaism  
  
RUN git checkout 'tags/v4.2.1'  
  
RUN go install -ldflags "-X main.Version="`git describe --tags` ./cmd/...  
  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
  
ENTRYPOINT ["/root/entrypoint.sh"]  

