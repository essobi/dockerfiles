FROM golang:1.4.1  
WORKDIR /go/src/github.com/tonistiigi/dnsdock  
  
RUN go get -v github.com/tools/godep  
  
ADD Godeps /go/src/github.com/tonistiigi/dnsdock/Godeps  
RUN godep restore  
  
ADD . /go/src/github.com/tonistiigi/dnsdock/  
RUN go install -ldflags "-X main.version `git describe --tags HEAD``[ $(git
status --porcelain --untracked-files=no | wc -l) -gt 0 ] && echo "-dirty"`"
./...  
  
ENTRYPOINT ["/go/bin/dnsdock"]  

