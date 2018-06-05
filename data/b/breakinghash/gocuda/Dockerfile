FROM nvidia/cuda:8.0-devel-ubuntu16.04  
  
RUN apt-get update  
RUN apt-get -y install python-software-properties software-properties-common
git-core  
  
RUN add-apt-repository ppa:longsleep/golang-backports && apt-get update  
RUN apt-get -y install golang-go  
  
RUN add-apt-repository ppa:masterminds/glide && apt-get update  
RUN apt-get install glide  
  
RUN mkdir -p /go/src  
ENV GOPATH=/go  
  
ENV CGO_CFLAGS="-I /usr/local/cuda-8.0/targets/x86_64-linux/include"  
ENV CGO_LDFLAGS="-L /usr/local/cuda-8.0/targets/x86_64-linux/lib"  
ADD . /build  
  
ENTRYPOINT /build/build.sh  

