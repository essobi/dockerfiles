FROM golang  
ADD . /go/src/github.com/kiyor/shadowsocks-go  
RUN cd /go/src/github.com/kiyor/shadowsocks-go/cmd/shadowsocks-server && \  
go get && \  
go install github.com/kiyor/shadowsocks-go/cmd/shadowsocks-server  
  
EXPOSE 1987  
ENTRYPOINT ["/go/bin/shadowsocks-server","-p","1987"]  

