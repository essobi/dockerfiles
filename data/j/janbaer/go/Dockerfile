FROM golang:1.8-alpine  
  
MAINTAINER Jan Baer  
  
# Install base packages  
RUN apk update && apk upgrade && \  
apk add bash curl wget tree git  
  
ENV GOBIN $GOPATH/bin  
ENV GOSRC $GOPATH/src  
  
RUN go get -u -buildmode=exe -ldflags '-s -w' \  
golang.org/x/tools/cmd/benchcmp \  
golang.org/x/tools/cmd/bundle \  
golang.org/x/tools/cmd/callgraph \  
golang.org/x/tools/cmd/cover \  
golang.org/x/tools/cmd/digraph \  
golang.org/x/tools/cmd/eg \  
golang.org/x/tools/cmd/fiximports \  
golang.org/x/tools/cmd/godex \  
golang.org/x/tools/cmd/godoc \  
golang.org/x/tools/cmd/goimports \  
golang.org/x/tools/cmd/gomvpkg \  
golang.org/x/tools/cmd/gorename \  
golang.org/x/tools/cmd/gotype \  
golang.org/x/tools/cmd/html2article \  
golang.org/x/tools/cmd/present \  
golang.org/x/tools/cmd/ssadump \  
golang.org/x/tools/cmd/stress \  
golang.org/x/tools/cmd/stringer \  
golang.org/x/tools/cmd/tip \  
golang.org/x/tools/refactor/eg \  
golang.org/x/tools/refactor/importgraph \  
golang.org/x/tools/refactor/rename \  
golang.org/x/tools/refactor/satisfy \  
  
github.com/rogpeppe/godef \  
github.com/tools/godep \  
github.com/nsf/gocode \  
github.com/kisielk/errcheck \  
github.com/golang/lint/golint \  
github.com/jstemmer/gotags \  
github.com/dougm/goflymake \  
github.com/golang/mock/mockgen \  
github.com/alecthomas/gometalinter && \  
  
gometalinter --install --update  
  
RUN mkdir $GOSRC/github.com/janbaer  
  
COPY .aliases .gitconfig .gitignore .bashrc /home/  
  
ENV HOME /home  
  
WORKDIR /home  
  
# Define bash as default command  
CMD ["/bin/bash"]  

