FROM golang:latest  
  
RUN mkdir -p /etc/gometalinter  
ADD config.json /etc/gometalinter/config.json  
  
RUN go get github.com/kyoh86/scopelint && \  
go get github.com/alecthomas/gometalinter && \  
go get github.com/haya14busa/reviewdog/cmd/reviewdog && \  
go get github.com/haya14busa/goverage && \  
gometalinter --install  

