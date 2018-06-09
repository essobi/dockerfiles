FROM golang:alpine  
MAINTAINER "Mark Maglana <mmaglana@gmail.com>"  
ENV PACKER_DEV=1  
RUN apk add --update git bash  
RUN go get github.com/mitchellh/gox  
RUN go get github.com/mitchellh/packer  
  
WORKDIR $GOPATH/src/github.com/mitchellh/packer  
  
RUN git remote add relaxdiego https://github.com/relaxdiego/packer.git && \  
git fetch relaxdiego 2>&1 && \  
git checkout -b ovf-export relaxdiego/ovf-export 2>&1 && \  
/bin/bash scripts/build.sh  
  
WORKDIR $GOPATH  
ENTRYPOINT ["bin/packer"]  

