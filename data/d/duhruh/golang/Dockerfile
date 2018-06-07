FROM centos:7  
ENV GOLANG_VERSION 1.10  
ENV GO_REL_ARCH linux-amd64  
  
RUN curl -fsSL "https://golang.org/dl/go$GOLANG_VERSION.$GO_REL_ARCH.tar.gz"
-o go.tar.gz;  
RUN tar -C /usr/local -xzf go.tar.gz;  
RUN rm go.tar.gz;  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN go version  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  

