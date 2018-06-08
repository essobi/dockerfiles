FROM golang:1.4  
MAINTAINER Stephen Caraher <moskvax@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libprotobuf-dev libleveldb-dev libgeos-dev \  
\--no-install-recommends  
  
RUN ln -s /usr/lib/libgeos_c.so /usr/lib/libgeos.so  
  
WORKDIR $GOPATH  
RUN go get github.com/tools/godep  
RUN git clone https://github.com/omniscale/imposm3
src/github.com/omniscale/imposm3  
RUN cd src/github.com/omniscale/imposm3 && godep go install ./...  
  
ENTRYPOINT ["imposm3"]  

