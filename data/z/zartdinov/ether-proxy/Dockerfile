FROM alpine:3.3  
ENV GOPATH /home/go  
ENV PACKAGE github.com/sammy007/ether-proxy  
  
RUN apk --update add -ut build-deps \  
go \  
git \  
g++  
  
RUN git clone https://$PACKAGE.git $GOPATH/src/$PACKAGE && \  
cd $GOPATH/src/$PACKAGE && \  
go get; exit 0 && \  
go build -o /bin/ether-proxy -ldflags "-s" main.go  
  
RUN rm -rf $GOPATH && \  
apk del --purge build-deps  
  
ENTRYPOINT ["/bin/ether-proxy"]  

