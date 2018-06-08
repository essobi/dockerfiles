FROM golang:1.10.1-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
# installs the ginkgo CLI  
go get github.com/onsi/ginkgo/ginkgo; \  
# fetches the matcher library  
go get github.com/onsi/gomega;  
COPY rootfs/go/src/codewars /go/src/codewars  
RUN go install codewars/reporter  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
GOPATH=$GOPATH:/home/codewarrior/go  

