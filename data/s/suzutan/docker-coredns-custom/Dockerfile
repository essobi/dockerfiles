FROM golang:1.10.1  
  
RUN go get github.com/coredns/coredns && \  
go get github.com/Eun/coredns-ipecho && \  
go get github.com/serverwentdown/alias && \  
cd /go/src/github.com/coredns/coredns && \  
echo "ipecho:github.com/Eun/coredns-ipecho" >> plugin.cfg && \  
echo "alias:github.com/serverwentdown/alias" >> plugin.cfg && \  
go generate && \  
go build && \  
cp ./coredns /coredns  
  
ENTRYPOINT [ "/coredns" ]  

