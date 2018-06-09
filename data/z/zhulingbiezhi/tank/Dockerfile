FROM golang:latest  
  
MAINTAINER huhai <zhulingbiezhi@gmail.com>  
  
WORKDIR $GOPATH/src/tank  
  
RUN cd $GOPATH; \  
mkdir src; \  
mkdir bin; \  
cd src; \  
git clone https://github.com/zhulingbiezhi/tank.git -b master; \  
cd tank; \  
go build  
  
EXPOSE 8080  
ENTRYPOINT ["./tank"]  

