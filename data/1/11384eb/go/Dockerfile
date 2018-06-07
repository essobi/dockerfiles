FROM golang:alpine  
  
RUN apk add -U --no-cache curl gcc git musl-dev \  
&& mkdir /goraw && cd /goraw/ \  
&& curl https://storage.googleapis.com/golang/go1.8.src.tar.gz | tar xvz \  
&& cd go/src && export GOROOT_BOOTSTRAP=/usr/local/go \  
&& platforms="darwin;386 darwin;amd64 freebsd;386 freebsd;amd64 freebsd;arm
linux;386 linux;amd64 linux;arm windows;386 windows;amd64" \  
&& for platform in ${platforms}; do goos=`echo $platform | cut -d \; -f 1` &&
goarch=`echo $platform | cut -d \; -f 2` \  
&& GOOS=$goos GOARCH=$goarch sh ./make.bash --no-clean 2>&1; done \  
&& cd /go && export GOPATH=$(pwd)  

