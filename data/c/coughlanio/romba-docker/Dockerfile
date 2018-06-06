FROM alpine:latest  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk --update --no-cache add git g++ zlib zlib-dev mercurial leveldb
leveldb-dev go  
  
ENV GOPATH=$HOME/go  
ENV PATH=$GOPATH/bin:$PATH  
  
RUN go get github.com/uwedeportivo/romba/cmds/rombaserver  
RUN go get github.com/uwedeportivo/romba/cmds/romba  
  
WORKDIR /romba  
  
ADD start.sh .  
  
ENTRYPOINT ["sh", "start.sh"]  

