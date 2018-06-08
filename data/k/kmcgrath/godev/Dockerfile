FROM golang:1.9  
  
# godep and go-vim binaries  
RUN go get -u \  
github.com/golang/dep/cmd/dep \  
github.com/nsf/gocode \  
github.com/alecthomas/gometalinter \  
golang.org/x/tools/cmd/goimports \  
golang.org/x/tools/cmd/guru \  
golang.org/x/tools/cmd/gorename \  
github.com/golang/lint/golint \  
github.com/rogpeppe/godef \  
github.com/kisielk/errcheck \  
github.com/jstemmer/gotags \  
github.com/klauspost/asmfmt/cmd/asmfmt \  
github.com/fatih/motion \  
github.com/zmb3/gogetdoc \  
github.com/josharian/impl  
  
# vim and janus  
RUN apt-get update && apt-get install -y \  
vim \  
rake \  
ack-grep \  
ctags \  
git \  
jq \  
&& curl -L https://bit.ly/janus-bootstrap | bash  

